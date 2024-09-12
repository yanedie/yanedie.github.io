---
created: 2024-07-23T13:59
updated: 2024-08-16T20:23
---
# 什么是 Hooks

假设你有一个智能家居系统。原本，当有人按门铃时，只会发出声音。现在你想要增加新功能：当有人按门铃时，除了发出声音，还要给你的手机发送通知，并拍摄一张访客的照片。

在这个场景中，你可以在“按门铃"这个事件上添加 hooks。这些 hooks 会在门铃被按下时触发，执行发送通知和拍照的操作，而不需要改变门铃原有的发声功能。

好比网页上有个按钮，按钮都可以点击（原本的功能没变），但是有的按钮点击后会提交信息，有的按钮点击后会清空信息（添加了新功能）。

点击事件之所以有不同的响应，是因为我们分配一个在点击事件发生时运行的函数，这些函数就是 hooks 函数，允许我们在不修改原有代码的情况下，在特定的时机插入新的功能或行为。这种机制使得程序更加灵活，易于扩展和定制。

## MkDocs 中的 Hooks 函数

MkDocs 中的 Hooks 函数允许我们在文档网站构建过程的不同阶段（事件）运行自定义代码，来实现特定的需求。

这些 Hooks 类似于刚刚谈到的一般 Hooks 概念，但专门应用于 MkDocs 的文档生成流程。我们可以自定义文档生成过程，添加新功能或集成第三方工具。
### 事件类型

MkDocs 的 Hooks 函数会在不同的事件发生时执行，这些事件包括[全局事件](https://www.mkdocs.org/dev-guide/plugins/#global-events)、[页面事件](https://www.mkdocs.org/dev-guide/plugins/#page-events)和[模板事件](https://www.mkdocs.org/dev-guide/plugins/#template-events)。事件也有发生的顺序，有的在页面生成前运行，有的在生成后运行，还有的在整个网站构建完成后运行。

以下是几种比较常见的事件，你可以根据需要选择合适的事件：

1. **on_pre_build**: 在构建过程开始之前触发
2. **on_config**: 用于修改配置文件的内容
3. **on_files**: 允许修改要处理的文件集合
4. **on_nav**: 用于修改目录
5. **on_page_markdown**: 允许修改页面的 Markdown 内容
6. **on_page_content**: 在 Markdown 转换为 HTML 后触发，允许修改 HTML
7. **on_post_build**: 在构建过程完成后触发

比如我们想要去除网页上的动图，那么有两个事件可以选择，一个是 `on_page_markdown`，另一个是 `on_page_content`。

注意：以上操作不会修改本地文件，只是修改了程序读取时的内容。

这里不一一列举，具体可以先看[官网对 Hook 的介绍](https://www.mkdocs.org/user-guide/configuration/#hooks)，再看[所有的事件](https://www.mkdocs.org/dev-guide/plugins/#events) ，对事件的作用、需要的参数、参数对象的属性和方法、返回值都有说明。

## 用法

在配置文件中添加，其中 `my_hooks` 为 Python 脚本的名称，与配置文件同一目录，可以分别添加多个脚本便于区分和维护：

```yaml
hooks:
	- my_hooks.py
	- update_config.py
	- remove_gif.py
	...
```

这是一个简单案例，该案例在 MkDocs 读取 Markdown 时触发，替换 markdown 文本：

```python title="my_hooks.py"
def on_page_markdown(markdown, page, config, files)
    return markdown.replace('shining', 'SHINING')
```

比如 admonition，我们可以在 Markdown 文件写成通用的格式：
```
> 说明：说明的内容
```

再利用 hooks 函数在 Markdown 转换为 HTML 前对"说明："进行预处理，免去转换格式或导入到其它软件语法不识别的问题。

我们也可以在一个 Python 文件内包含多个事件共同配合，以离线版网站为例：

- `on_config` 修改 `use_directory_urls` 的值和 LOGO 等文件路径'。 
- `on_page_markdown` 利用正则匹配图片链接，下载至 common 文件夹，同时替换图片链接为相对路径。

此外，由于脚本由于不位于 docs 文件夹内，修改后 MkDocs 不会热重载，但是我们可以把脚本放在一个名为 hooks 的文件夹内，并在配置文件中监听该文件夹变动，从而实现修改脚本后重新加载。

```yaml
watch:
  - hooks
```

附：

``` python fold
def on_config(config):
    """
    `config`事件是文档构建时调用的第一个事件，在加载和验证配置文件后立即运行。对配置文件（即YAML文件）的任何修改都应该在这里进行。
    """
    return config

def on_pre_build(config):
    """
    `pre_build`事件不会改变任何变量。使用此事件在开始构建之前调用脚本。
    """

def on_files(files, config):
    """
    从docs文件夹获取文件集合之后调用[`files`](https://www.mkdocs.org/dev-guide/api/#mkdocs.structure.files.Files)事件。使用此事件可在集合中添加、删除或更改文件。
    注意，[Page对象](https://www.mkdocs.org/dev-guide/themes/#mkdocs.structure.pages.Page)还没有与集合中的[`file`对象](https://www.mkdocs.org/dev-guide/api/#mkdocs.structure.files.File)相关联。使用页面事件操作特定于页面的数据。
    参见 https://www.mkdocs.org/user-guide/plugins/#on_nav
    """
    return files

def on_nav(nav, config, files):
    """
    在创建目录后调用nav事件。可用于更改目录。
    参见 https://www.mkdocs.org/user-guide/plugins/#on_nav
    """
    return nav

def on_pre_page(page, config, files):
    """
    在对主题页执行任何操作之前调用`pre_page`事件，并可用于更改[Page实例](https://www.mkdocs.org/dev-guide/themes/#mkdocs.structure.pages.Page)。
    """
    return page

def on_page_read_source(page, config):
    """
    过时。推荐使用`on_page_markdown`事件。
    """
    return ""

def on_page_markdown(markdown, page, config, files):
    """
    在从文件加载页面标记后调用``事件，可用于更改标记源文本。元数据已被剥离，并作为页面可用。在这一点上。
    """
    return markdown

def on_page_content(html, page, config, files):
    """
    page_content 事件将在将 Markdown 文本渲染到HTML之后调用。
    （但是在传递到模板之前），可以用于更改页面的HTML主体。
    参见 https://www.mkdocs.org/user-guide/plugins/#on_page_content
    """
    return html

def on_env(env, config, files):
    return env

def on_page_context(context, page, config, nav):
    """
    在创建页面的上下文之后调用页上下文事件。
    它只能用于更改特定页面的上下文。
    参见 https://www.mkdocs.org/user-guide/plugins/#on_page_context
    """
    return context

def on_post_page(output, page, config):
    return output

def on_post_build(config):
    """
    post_build 事件不会改变任何变量。使用此事件在文档构建完成后调用脚本。

    参见 https://www.mkdocs.org/user-guide/plugins/#on_post_build
    """
    return
```
