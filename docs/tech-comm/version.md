# 旧版本软件看新文档？不存在的

最近在优化软件的文档体验，遇到一个挺有意思的问题：软件内嵌的帮助文档链接是固定的，但软件版本迭代快，旧版本用户点开帮助，直接跳转到最新文档，用户体验不太好！

作为技术文档工程师，我觉得这事儿必须安排明白！旧版本软件也能看到对应的文档啦，再也不怕用户一脸懵逼了！

问题的核心在于：所有版本的软件都使用同一个 URL，导致无法区分不同版本的用户，从而无法提供对应的文档版本。

经过一番头脑风暴，决定采用“曲线救国”的方式，主要分为以下几个步骤：

1. 链接增加版本号查询参数

    比如链接是`docs.abc.com`，加上查询参数（URLSearchParams），变成`docs.abc.com?version=1.0.0`，现在可以使用 JavaScript 解析 URL 获取到版本信息。

    ``` javascript
    const urlParams = new URLSearchParams(location.search);
    const version = urlParams.get("version");
    ```

    这一步需要与软件开发工程师合作，在每次软件发布前，提供带有版本号参数的 URL 给他们。

    这样，每个版本的软件都对应一个带有特定 version 参数的 URL。

2. HTML 头部添加版本号 Meta 标签

    仅仅在 URL 上添加版本号还不够，还需要在文档网站上也添加版本信息，以便前端代码能够读取和判断。

    在文档网站打包时，我修改了文档的构建脚本（我们使用的是 MkDocs），让它在生成 HTML 文件时，自动将版本信息添加到<meta>标签中。

    ``` html
    <meta name="version" content="1.0.0">
    ```

3. 编写 JavaScript 代码

    实现以下逻辑：

    获取 URL 中的 version 参数。
    获取<meta>标签中的 version 值。
    比较两个版本号。
    如果版本号不一致，则显示提示信息，并提供跳转到对应版本文档的链接。

    ``` javascript
    // 获取 URL 参数
    function getQueryParam(name) {
    const urlParams = new URLSearchParams(location.search);
    return urlParams.get(name);
    }

    // 获取 meta 标签内容
    function getMetaContent(name) {
    const metaTag = document.querySelector(`meta[name="${name}"]`);
    return metaTag ? metaTag.content : null;
    }

    // 获取软件内嵌 URL 版本
    const softwareVersion = getQueryParam('version');
    // 获取最新 URL 版本
    const documentVersion = getMetaContent('version');

    // 比较版本
    if (softwareVersion !== documentVersion && softwareVersion !== null && documentVersion !== null) {
    // 进行后续自定义操作

    // 比如提示用户
    const message = `当前文档为最新版本，与您的软件版本（${softwareVersion}）不匹配。请<a href="/document/${softwareVersion}">点击这里</a>查看对应版本的文档。`;

    const warningDiv = document.createElement('div');
    warningDiv.innerHTML = message;
    warningDiv.style.cssText = `background-color: yellow; padding: 10px; text-align: center;`;
    document.body.insertBefore(warningDiv, document.body.firstChild);
    }

    // 也可以直接跳转等等.....
    ```

这个方案仍然有改进的空间，例如可以考虑进一步提高自动化程度，例如软件开发自动添加查询参数而不用手动提供等。
