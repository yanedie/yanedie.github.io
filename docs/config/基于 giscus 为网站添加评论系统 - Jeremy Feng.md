---
created: 2023-09-16T18:57:28 (UTC +08:00)
tags: [mkdocs]
source: https://fengchao.pro/blog/comment-system-with-giscus/?h=%E8%AF%84%E8%AE%BA
author: Jeremy Feng
---
giscus 是一个简单易用的评论系统，它使用 GitHub Discussion 的作为存储和管理评论的后端。网站的访客可以使用 GitHub 账号登录并发表评论，当有新评论时 GitHub 还会用邮件通知网站的主人。

本文记录了基于 giscus 为网站添加评论系统的过程。整个过程还算比较顺利，但中途遇到的关于一键配置多个页面展示评论系统的问题也困扰了我很久。将其记录于此，希望能帮助自己和他人。

![image-20230722131239896](https://fengchao.pro/blog/assets/2023-07-21-comment-system-with-giscus/index-image/image-20230722131239896.png)

## 配置 giscus

根据 Material for MkDocs 官方提供的[教程](https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/)，完成以下步骤：

1.  安装 [giscus GitHub App](https://github.com/apps/giscus)。这一步只需要在 GitHub 官网上点击安装即可。
    
2.  访问 [giscus](https://giscus.app/) 官网，配置与 giscus 评论系统关联的 GitHub 仓库。
    
    请确保：
    
    1.  **该仓库是[公开的](https://docs.github.com/en/github/administering-a-repository/managing-repository-settings/setting-repository-visibility#making-a-repository-public)**，否则访客将无法查看 Discussion。
    2.  **[giscus](https://github.com/apps/giscus) app 已安装**，否则访客将无法评论和回应。
    3.  **Discussions** 功能已[在你的仓库中启用](https://docs.github.com/en/github/administering-a-repository/managing-repository-settings/enabling-or-disabling-github-discussions-for-a-repository)。
    
    存放评论的仓库与搭建网站的仓库不是必须相同的
    
    注意，存放评论的仓库与搭建网站的仓库不是必须相同的。前者必须是 Public 的仓库（否则网站访客就无法看到评论信息），但后者可以是 Private 的仓库。当然，这两者也可以是同一仓库。
    
    这一步会得到类似于下面这种格式的配置代码：
    ```
    <script
    src="https://giscus.app/client.js"
    data-repo="<username>/<repository>"
    data-repo-id="..."
    data-category="..."
    data-category-id="..."
    data-mapping="pathname"
    data-reactions-enabled="1"
    data-emit-metadata="1"
    data-theme="light"
    data-lang="en"
    crossorigin="anonymous"
    async
    >
    </script>
    ```

3.  参照 [override the `comments.html` partial](https://squidfunk.github.io/mkdocs-material/customization/#overriding-partials) 的方法，覆盖原有的空白的 `comments.html`。它的层级结构为：
    
    ![image-20230722132437183](https://fengchao.pro/blog/assets/2023-07-21-comment-system-with-giscus/index-image/image-20230722132437183.png)
    
    并添加以下内容：
    ```
        {% if page.meta.comments %}
        <h2 id="__comments">{{ lang.t("meta.comments") }}</h2>
        <!-- Insert generated snippet here -->
    
        <!-- Synchronize giscus theme with palette -->
        <script>
                var giscus = document.querySelector("script[src*=giscus]")
    
            /* Set palette on initial load */
            var palette = __md_get("__palette")
            if (palette && typeof palette.color === "object") {
                var theme = palette.color.scheme === "slate" ? "dark" : "light"
                giscus.setAttribute("data-theme", theme) // (1)!
      }
    
            /* Register event handlers after documented loaded */
            document.addEventListener("DOMContentLoaded", function() {
                var ref = document.querySelector("[data-md-component=palette]")
                ref.addEventListener("change", function() {
                    var palette = __md_get("__palette")
                    if (palette && typeof palette.color === "object") {
                        var theme = palette.color.scheme === "slate" ? "dark" : "light"
    
                        /* Instruct giscus to change theme */
                        var frame = document.querySelector(".giscus-frame")
                        frame.contentWindow.postMessage(
                            { giscus: { setConfig: { theme } } },
                            "https://giscus.app"
                        )
                    }
                })
            })
        </script>
        {% endif %}
    ```
    
    将高亮的那一行代码替换成第 2 步得到的配置代码。
    
4.  在需要展示评论的文档的 `yaml` 中，添加 `comments: true`：
    
    YAML
    
    ```
    ---
    comments: true
    ---
    
    ```
    

## 效果展示

至此，你已经能看到页面底部展现了评论系统：

![image-20230722131239896](https://fengchao.pro/blog/assets/2023-07-21-comment-system-with-giscus/index-image/image-20230722131239896.png)

此外，当有新评论或反应时，GitHub 会发送邮件通知：

![image-20230722131357485](https://fengchao.pro/blog/assets/2023-07-21-comment-system-with-giscus/index-image/image-20230722131357485.png)

## 一键配置多个页面展示评论系统

[官方教程](https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/)的最后提到，可以用 [built-in meta plugin](https://squidfunk.github.io/mkdocs-material/reference/#built-in-meta-plugin) 实现一键配置多个页面展示评论系统，这样就不需要在每个文档的 `yaml` 中添加 `comments: true`了。

![image-20230722130523736](https://fengchao.pro/blog/assets/2023-07-21-comment-system-with-giscus/index-image/image-20230722130523736.png)

`meta` 插件在撰写本文时还是 Insiders 版本，如果你使用的是 Insiders 版本，可以在 `mkdocs.yaml` 中添加：

然后在文档的文件夹下新建一个 `.meta.yml` 文件，这将使得该文件夹内的所有文档对应的页面都能展示评论系统。

`.meta.yml` 文件中不需要添加 `---`

我最初在 `.meta.yml` 文件中添加的是

YAML

```
---
comments: true
---

```

实际上只需要添加这一行

如果这个文件夹中有某些页面不需要展示评论系统，只需要手动在这些页面的`yaml` 中添加 `comments: false` 即可。
