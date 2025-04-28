---
title: Vale + VS Code 实现自动化风格检查
categories:
  - docs as code
tags:
  - linter
  - style guide
created: 2023-09-19T01:39
updated: 2024-02-16T16:25
---

# 在 VS Code 中使用 Vale 自动检查风格和语法

## 使用 Chocolatey 安装 Vale

Chocolatey 是一个用于 Windows 的软件包管理器，简化了安装、更新和管理软件应用程序的过程。它提供了一个命令行界面（CLI），让用户可以轻松搜索、安装和卸载软件包。Chocolatey 自动化了从各种来源（如官方网站或软件仓库）下载软件的过程，并为你处理安装和配置步骤。

使用 Chocolatey，你可以管理开源和商业软件包，包括开发工具、生产力应用程序、实用工具等。它使你能够通过自动安装多个软件包一次性设置和配置 Windows 环境，这在配置新计算机或在多台计算机上部署应用程序时特别有用。

要在 Windows 上使用 Chocolatey 安装 Vale，请按照以下分步说明操作：

1. **安装 Chocolatey：**

    a. 按 `Win+X` 键，然后选择“Windows 终端（管理员）”，或者在开始菜单中搜索“Windows PowerShell”，右键单击它并选择“以管理员身份运行”。

    b. 在 PowerShell 窗口中，确保你已设置正确的执行策略，通过运行以下命令来设置：

        ```shell
        Set-ExecutionPolicy Bypass -Scope Process -Force
        ```

    c. 现在，运行以下命令来安装 Chocolatey：

        ```shell
        iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
        ```

    d. 安装完成后，关闭 PowerShell 窗口。

2. **安装 Vale：**

    a. 以管理员身份打开一个新的 PowerShell 窗口（如步骤 1a 所述）。

    b. 运行以下命令安装 Vale：

        ```shell
        choco install vale
        ```

    c. 等待安装完成。Chocolatey 会自动为你下载并安装 Vale。

3. **验证安装：**

    a. 关闭并重新以管理员身份打开 PowerShell 窗口。

    b. 运行以下命令检查 Vale 版本：

        ```shell
        vale -v
        ```

    如果 Vale 安装正确，你应该在输出中看到版本号。

4. **配置 Vale：**

    a. 要获得初始 Vale 配置，你需要克隆或下载 [Vale-boilerplate](https://github.com/errata-ai/vale-boilerplate)。

    b. [点此下载](https://github.com/errata-ai/vale-boilerplate/archive/refs/heads/master.zip)，如果你要克隆，请确保电脑上安装 Git，然后在命令行中输入：

        ```
        git clone https://github.com/errata-ai/vale-boilerplate.git
        ```

    c. 用文本编辑器打开 `.vale.ini` 文件，并根据你的需求进行自定义。你也可以在[Config Generator](https://vale.sh/generator/)中创建自定义配置，并将代码块复制粘贴覆盖 .vale.ini 文件，然后运行`vale sync`对其进行初始化。

    d. 由于国内防火墙（GFW）问题，此命令失效，即使通过网络代理也无法执行命令。你可以到 [Vale 风格指南仓库](https://github.com/errata-ai/packages#available-styles) 下载你所需要的风格指南到 Style 目录，并打开 .vale.ini，将文件夹名称添加到 BasedOnStyles 中。

5. **使用 Vale：**

   a. 现在，你可以使用 Vale 来检查文本文件中的风格和语法问题。要执行此操作，请在 vale 目录下打开 PowerShell 运行以下命令：

        ```shell
        vale "path\to\your\file.txt"
        ```

    b. 将 `C:\Vale-config\.vale.ini` 替换为你的配置文件的路径，将 `path\to\your\file.txt` 替换为你要检查的文本文件的路径。

    c. 你已成功在 Windows 上使用 Chocolatey 安装并配置了 Vale。[点此查看](#在-vs-code-中使用-vale)使用 VS Code 使用 Vale 进行自动化检查。

6. **升级 Vale：**

    你可以使用 Chocolatey 更新 Vale。

    a. 确保你已经安装了 Vale。

        ```shell
        vale -v
        ```

    此命令显示安装的 Vale 版本。

    b. 确保你安装了 Chocolatey。

        ```shell
        choco -v
        ```

    此命令显示安装的 Chocolatey 版本。

    c. 更新 Vale 版本。

        ```shell
        choco upgrade vale
        ```

    此命令将 Vale 更新为存储为 Chocolatey 包的最新版本的 Vale 。

---

## 在 VS Code 中使用 Vale

要在 VS Code 中配置扩展插件 Vale，你需要按照以下步骤进行操作：

1. 安装 Vale 插件：打开 VS Code 并进入扩展视图（可以使用快捷键 `Ctrl+Shift+X` 或点击左侧活动栏中的插件图标）。在搜索栏中输入"Vale"，找到Vale插件并点击"安装"按钮进行安装。

2. 配置 Vale 插件：安装完成后，打开 VS Code 的设置（可以使用快捷键 `Ctrl+，`或点击左下角齿轮图标）。在设置中搜索"vale.valeCLI.config"，在输入框中输入配置文件（.vale.ini）的绝对路径，比如`C:\Vale-config\.vale.ini`

3. 重新加载 VS Code 窗口，以使配置更改生效。

4. 现在，你已经成功配置了 Vale 扩展插件。它将在你编辑的文件中提供文本检查和风格建议。当你在 VS Code 中打开任何 Markdown 文件时，Vale 会自动在有问题的单词或句子下面划线。你可以将鼠标悬停在带下划线的文本上或转到VS Code 底部的问题选项卡。

---

## 创建自己的风格指南

要添加你自己的规则：

1. 使用你自己的风格指南名称创建一个目录。例如，my-styleguide。

2. 将 my-styleguide 目录复制到包含所有其他样式指南的 Style 目录。

3. 在 VS Code 中打开 .vale.ini 配置文件。

4. 将你的 my-styleguide 文件名添加到 BasedOnStyles 中。

5. 保存更改。

6. 将编辑好的 YML 文件（即规则）添加到 my-styleguide 目录中。
