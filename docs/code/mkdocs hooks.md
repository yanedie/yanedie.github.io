---
created: 2024-07-23T13:59
updated: 2024-07-25T01:47
---
# 什么是 Hooks

假设你有一个智能家居系统。原本，当有人按门铃时，只会发出声音。现在你想要增加新功能：当有人按门铃时，除了发出声音，还要给你的手机发送通知，并拍摄一张访客的照片。

在这个场景中，你可以在“按门铃"这个事件上添加 hooks。这些 hooks 会在门铃被按下时触发，执行发送通知和拍照的操作，而不需要改变门铃原有的发声功能。

hooks 就像是程序中预先设置的"挂钩"。它们允许我们在不修改原有代码的情况下，在特定的时机插入（挂上）新的功能或行为。这种机制使得程序更加灵活，易于扩展和定制。

## 使用 Hooks 的优势

- **灵活性**：允许在不修改 MkDocs 核心代码的情况下自定义文档生成过程
- **可扩展性**：易于添加新功能或集成第三方工具
- **非侵入性**：不会影响 MkDocs 的核心功能，可以随时启用或禁用
## Mkdocs 中的 Hooks

MkDocs 中的 Hooks 允许我们在文档生成过程的不同阶段（事件）插入自定义代码，以修改或增强默认行为。这些 Hooks 类似于刚刚谈到的一般 Hooks 概念，但专门应用于 MkDocs 的文档生成流程。

### Hooks 的类型

MkDocs 的 Hooks 能够在不同的事件发生时运行，包括[全局事件](https://www.mkdocs.org/dev-guide/plugins/#global-events)、[页面事件](https://www.mkdocs.org/dev-guide/plugins/#page-events)和[模板事件](https://www.mkdocs.org/dev-guide/plugins/#template-events)，Hooks 脚本内可以包含这些事件，有的在页面生成前运行，有的在生成后运行，还有的在整个网站构建完成后运行。你可以根据需要选择合适的事件进行触发，以下是几种比较常见的事件：

1. **on_pre_build**: 在构建过程开始之前触发
2. **on_config**: 用于修改配置文件的内容
3. **on_files**: 允许修改要处理的文件集合
4. **on_nav**: 用于修改目录
5. **on_page_markdown**: 允许修改页面的 Markdown 内容
6. **on_page_content**: 在 Markdown 转换为 HTML 后触发，允许修改 HTML
7. **on_post_build**: 在构建过程完成后触发

这里不一一列举，具体可以先看[官网对 Hook 的介绍](https://www.mkdocs.org/user-guide/configuration/#hooks)，再看[所有的事件](https://www.mkdocs.org/dev-guide/plugins/#events) 。

## 如何使用 Hooks？

在配置文件中添加，其中 `my_hooks` 为 hooks 脚本的名称，可以添加多个脚本以模块化：

```yaml
hooks:
	- my_hooks.py
```

然后 `my_hooks.py` 文件可以包含不止一个事件，例如：

```python title="my_hooks.py"
def on_page_markdown(markdown, page, config, files)
    return markdown.replace('shining', 'SHINING')
```

该脚本将获取到的 Markdown 文本中所有 shining 替换为 SHINING。


- `on_config` Hook 添加支持的语言列表到配置中。
- `on_files` Hook 为每种语言创建新的Markdown文件。
- `on_page_markdown` Hook 使用翻译API翻译页面内容。
- `on_nav` Hook 为每种语言创建单独的导航部分。

hooks 由于不位于 docs 文件夹内，修改后 MkDocs 不会热重载，但是我们可以把钩子脚本放在一个名为 hooks 的文件夹内，并在配置文件中监听该文件夹，从而实现修改钩子脚本后重新加载。

```yaml
watch:
  - hooks
```

**MkDocs 1.6 中的新功能。**
如果一个 hooks 文件旁边有一个`foo.py`文件，它可以使用普通的 Python 语法`import foo`来访问其函数。
在旧版本的 MkDocs 中，需要一个变通的方法：将路径添加到 `sys.path` 中。

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
