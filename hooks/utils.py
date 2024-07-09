import logging, re, os
import autocorrect_py as autocorrect
from datetime import datetime
log = logging.getLogger('mkdocs')

# 生成更语义化的链接，有助于 SEO
def on_files(files, config):
    for f in files:
        if f.is_documentation_page():
            # 删除空格、括号并将路径中的反斜杠替换为正斜杠
            f.abs_dest_path = os.path.normpath(f.abs_dest_path.replace(" ", "-").replace("(", "").replace(")", "").replace("\\", "/")).replace("\\", "/").lower()
            f.dest_path = os.path.normpath(f.dest_path.replace(" ", "-").replace("(", "").replace(")", "").replace("\\", "/")).replace("\\", "/").lower()
            f.url = f.dest_path.replace("%20", "-").replace("\\", "/").lower()
            # 删除数字序号
            f.abs_dest_path = re.sub(r'\d+\.', '', f.abs_dest_path)
            f.dest_path = re.sub(r'\d+\.', '', f.dest_path)
            f.url = re.sub(r'\d+\.', '', f.url)
    return files

# obsidian code styler 插件高亮代码行规则转换成 mkdocs-material 高亮代码行规则
def on_page_markdown(markdown, page, config, files):
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
    markdown = autocorrect.format(re.sub(r'(```\w+) fold(.*)', remove_fold, markdown))

    # 文章底部添加最后更新时间
    if re.search(r'blog/index.html|tags/index.html', page.url):
        return markdown
    else:
        if 'created' in page.meta:
            created_time_str = page.meta['created']
            created_dt = datetime.strptime(created_time_str, "%Y-%m-%dT%H:%M")
            created_time = created_dt.strftime("%Y-%m-%d %H:%M")
            creation_note = f':material-clock-plus-outline:{{title="创建时间"}} <span style="font-size:.68rem;color:var(--md-default-fg-color--light)">{created_time}<span>'
            markdown = f'{markdown}\n\n{creation_note}'
        if 'updated' in page.meta:
            time_str = page.meta['updated']
            dt = datetime.strptime(time_str, "%Y-%m-%dT%H:%M")
            last_updated_time = dt.strftime("%Y-%m-%d %H:%M")
            revision_note = f':material-clock-edit-outline:{{title="最后更新"}} <span style="font-size:.68rem;color:var(--md-default-fg-color--light)">{last_updated_time}<span>'
            markdown = f'{markdown}\r{revision_note}'
        return markdown

