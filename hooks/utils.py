import logging, re, os
import autocorrect_py as autocorrect
from datetime import datetime
log = logging.getLogger('mkdocs')

# 生成更语义化的链接，有助于 SEO
def on_files(files, config):
    for f in files:
        if f.is_documentation_page():
            # 删除数字序号和序号后的空格
            f.abs_dest_path = re.sub(r'\d+\.', '', f.abs_dest_path).replace("\ ", "\\")
            f.dest_path = re.sub(r'\d+\.', '', f.dest_path).replace("\ ", "\\")
            f.url = re.sub(r'\d+\.', '', f.url).replace("/%20", "/")

            # 替换剩余的空格、括号并将路径中的反斜杠替换为正斜杠
            f.abs_dest_path = os.path.normpath(f.abs_dest_path.replace(" ", "-").replace("(", "").replace(")", "").replace("\\", "/")).replace("\\", "/").lower()
            f.dest_path = os.path.normpath(f.dest_path.replace(" ", "-").replace("(", "").replace(")", "").replace("\\", "/")).replace("\\", "/").lower()
            f.url = f.dest_path.replace("%20", "-").replace("\\", "/").lower()
    return files

# obsidian code styler 插件高亮代码行规则转换成 mkdocs-material 高亮代码行规则
def on_page_markdown(markdown, page, config, files):
    # 为所有页面开启评论
    page.meta['comments'] = True

    # # 以过滤后的文件名作为 frontmatter 的 title
    # filename = os.path.basename(page.file.src_path)
    # # 去除格式后缀
    # title = os.path.splitext(filename)[0]
    # 去掉数字和点
    # title = re.sub(r'^\d+\.\s*', '', title)
    # 下划线和横杠换成空格
    # page.meta['title'] = title

    # 替换 hl 的规则
    def replace_hl(match):
        hl_content = match.group(1)
        hl_lines = hl_content.replace(",", " ")
        return f'hl_lines="{hl_lines}"'

    # 使用正则表达式查找和替换 hl
    markdown = re.sub(r'hl:([\d,\-]+)', replace_hl, markdown)

    # 删除代码块第一行的 fold 和一个空格
    def remove_fold(match):
        before_fold = match.group(1)
        after_fold = match.group(2)
        return f'{before_fold}{after_fold}'

    # 查找并删除代码块第一行的 fold 和一个空格
    if page.file.src_uri != "nav.md":
        markdown = autocorrect.format(re.sub(r'(```\w+) fold(.*)', remove_fold, markdown))
        return markdown
