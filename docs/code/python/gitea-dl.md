---
created: 2023-09-19T14:11
updated: 2024-07-09T01:06
---
# 下载 Gitea 仓库分支文件

[Mkdocs-Macros](../mkdocs-plugins/mkdocs-macros/mkdocs-macros.md) 插件能够运行 python 脚本，还能够将 Markdown 转为 jinja 模板，这样能够做到数据与模板（样式）相分离。而在运行网站时，会自动加载 Mkdocs-Macros 插件。借此萌生了一个想法，爬取 Gitea[^1] 仓库的 Markdown 文件或者是变量文件（.yml）至本地网站目录，做到一方修改，多方同步。

!!! tip

    目前已经有现成的插件加载托管于外部服务器的 Markdown 源文件，但是与 Mkdocs-Macros 插件冲突，且只支持 Github 的私有仓库。在学会调接口后，着手对插件进行修改。修改完毕的插件已经发布在 pypi 上：<https://pypi.org/project/mkdocs-embed-markdown/>。现在增加了对 Gitea 私有仓库 的支持。

[^1]: Gitea 是一个开源的基于 Go 语言的 Git 托管服务，可以在本地部署用于管理代码仓库、代码贡献等功能，非常适合企业或组织内部使用，和 Github 类似。

## 源码

最初是使用 requests 模拟传递账号密码登陆，由于是明文保存，该方案不行。第二个版本是使用 cookie 登陆，但是需要在浏览器上定期登陆网站来保活，因此也不能够一劳永逸。最后，在查阅了大量资料以后，终于知道怎么调 Gitea 的官方 API 了。因此，有了最终版，使用 token 登陆。

前提条件：在 Gitea 的个人设置中找到**应用**，然后生成令牌（token），将令牌保存到系统变量中，名称为 GI_TOKEN。

=== "账号密码"

    ```
    import requests
    from bs4 import BeautifulSoup
    import os
    import re

    def login_session(username, password):
        """
        创建并返回登录会话。
        """
        login_url = "https://git.example.com/user/login"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        data = {
            "user_name": username,
            "password": password
        }

        session = requests.session()
        session.post(login_url, data=data, headers=headers)
        return session

    def save_file(session, url, file_path):
        """
        从给定的 URL 下载并保存文件。
        """
        response = session.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed download from {url}, status code: {response.status_code}")

    def download_files(session, target_url, output_folder):
        """
        从目标地址下载文件和文件夹，并将其保存到指定的输出文件夹中。
        """
        response = session.get(target_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            entries = soup.find_all('tr', class_='ready entry')

            for entry in entries:
                repo = soup.select_one('a[href*="/qa/"]').text.strip()
                branch = soup.select_one('[data-ref-name]')['data-ref-name']
                link = entry.find('a', href=re.compile(f'/qa/{repo}/src/'))
                if link:
                    href = link.get('href')
                    raw_url = f'https://git.example.com{href.replace("/src/", "/raw/")}'
                    file_name = link.text.strip()

                    # 判断是文件还是文件夹
                    if '.' in file_name:
                        save_file(session, raw_url, os.path.join(output_folder, file_name))
                    else:
                        # 如果是仓库链接，而非分支链接，其文件下载链接需要构造成分支链接
                        if target_url.endswith(f'/{repo}'):
                            target_url = f'{target_url}/src/branch/{branch}'
                            subfolder_url = f'{target_url}/{file_name}'
                        else:
                            # 如果是分支链接，直接和文件名拼接即可
                            subfolder_url = f'{target_url}/{file_name}'

                        subfolder_output = os.path.join(output_folder, file_name)

                        if not os.path.exists(subfolder_output):
                            os.makedirs(subfolder_output)

                        download_files(session, subfolder_url, subfolder_output)

        else:
            print(f"无法获取 {target_url}, 状态码：{response.status_code}")

    if __name__ == "__main__":
        # 输入 git.example.com 的个人帐户用户名、密码
        username = "test"
        password = "123456"

        # 输入要下载的 Git 链接
        target_url = ''

        # 输入要保存的文件夹名称（引号内放空就保存在同级目录。）
        output_folder = ''

        # 以下不用修改
        session = login_session(username, password)
        download_files(session, target_url, output_folder)
    ```

=== "Cookie"

    ```
    import requests
    import browser_cookie3
    from bs4 import BeautifulSoup
    import os
    import re

    def login_session(cookies=None):
        """
        创建并返回登录会话，传递浏览器保存的 cookie 数据。
        """
        session = requests.session()

        # 如果提供了浏览器保存的 cookie 数据，将其添加到会话中
        if cookies:
            session.cookies.update(cookies)

        return session

    def save_file(session, url, file_path):
        """
        从给定的 URL 下载并保存文件。
        """
        response = session.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
        else:
            print(f'无法从 {url} 下载，状态码：{response.status_code}')

    def download_files(session, target_url, output_folder):
        """
        从目标地址下载文件和文件夹，并将其保存到指定的输出文件夹中。
        """
        response = session.get(target_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # 通过 CSS 类名和 HTML 标签找到仓库文件列表
            entries = soup.find_all('tr', class_='ready entry')
            for entry in entries:
                # 通过 CSS 属性选择器来获取仓库名和分支名
                repo = soup.select_one('a[href*="/qa/"]').text.strip()
                branch = soup.select_one('[data-ref-name]')['data-ref-name']
                # 通过属性的值和正则表达式找到文件和文件夹的 <a> 标签
                link = entry.find('a', href=re.compile(f'/qa/{repo}/src/'))
                if link:
                    # 获取 <a> 标签 href 属性的值，即绝对路径
                    href = link.get('href')
                    # 然后拼接成原始文件的下载链接
                    raw_url = f'https://git.example.com{href.replace("/src/", "/raw/")}'

                    # 获取 <a> 标签内的字符串，即文件和文件夹的名称。
                    file_name = link.text.strip()
                    # 带 . 的是文件，不带 . 的是文件夹（也有可能是 .gitignore）。
                    if '.' in file_name:
                        # 如果是文件，则直接下载
                        save_file(session, raw_url, os.path.join(output_folder, file_name))
                    else:
                        # 如果是文件夹，分两种情况：
                        # 如果输入的是仓库名结尾的链接，那么文件夹的下载链接需要构造成分支链接
                        if target_url.endswith(f'/{repo}'):
                            target_url = f'{target_url}/src/branch/{branch}'
                            subfolder_url = f'{target_url}/{file_name}'
                        else:
                            # 如果输入的是分支链接，直接和文件名拼接即可
                            subfolder_url = f'{target_url}/{file_name}'

                        # 生成保存路径
                        subfolder_output = os.path.join(output_folder, file_name)

                        # 判断文件夹是否存在，不存在则创建
                        if not os.path.exists(subfolder_output):
                            os.makedirs(subfolder_output)

                        download_files(session, subfolder_url, subfolder_output)

        else:
            print(f'无法获取 {target_url}, 状态码：{response.status_code}')

    if __name__ == '__main__':
        target_url = ''

        # 输入要保存的文件夹名称，引号内放空会保存在同级目录。
        output_folder = 'test'

        # 以下不用修改
        access_cookie = browser_cookie3.edge()
        session = login_session(cookies = access_cookie)
        download_files(session, target_url, output_folder)
    ```

=== "Access token"

    ```
    def main():
        gt_token = os.getenv("GT_TOKEN")
        url = "https://git.example.com/raw/branch/owner/repo/branch/filepath"  # 请替换为实际的URL
        if "raw/branch" in url:
            if gt_token:
                parts = url.split("/")
                host = parts[2]
                owner = parts[3]
                repo = parts[4]
                branch = parts[7]
                branch_index = parts.index("branch")
                filepath = "/".join(parts[branch_index + 2:])
                file_url = f"{host}/api/v1/repos/{owner}/{repo}/raw/{filepath}?ref={branch}&token={gt_token}"
                url = file_url
        response = requests.get(url)
        if response.status_code == 200:
            with open(filepath, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed download from {url}, status code: {response.status_code}")

    if __name__ == "__main__":
        main()
    ```
