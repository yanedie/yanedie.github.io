import copy
import datetime
import re
import os
import logging
import requests
import subprocess
from urllib.parse import urlparse
import git
import pytz
import autocorrect_py as autocorrect
from jinja2 import Template, Environment, FileSystemLoader
from bs4 import BeautifulSoup

log = logging.getLogger('mkdocs')

# def on_page_content(html, page, config, files):
#     current_year = datetime.datetime.now().year
#     updated_html = html.replace('{{current_year}}', str(current_year))
#     return updated_html


# def on_env(env, config, files):
#     r = git.Repo(".")
#     tag = r.git.describe(tags=True)
#     hc = r.head.commit
#     commit_datetime_utc = r.head.commit.committed_datetime.astimezone(pytz.timezone("UTC"))
#     env.globals["git"] = {
#         # intended to be consistent with mkdocs-macros-plugin git info:
#         "author": hc.author.author,
#         "author_email": hc.author.email,
#         "commit": hc.hexsha,
#         "committer": hc.committer.name,
#         "committer_email": hc.committer.email,
#         "date": hc.committed_date,
#         "message": hc.message,
#         "short_commit": hc.hexsha[:7],
#         "tag": tag,

#         # bonus:
#         "datetime_utc": commit_datetime_utc,
#         }
#     log.info(f"Entering on_env hook; added {tag}")
#     return env

def get_latest_commit_info():
    try:
        # 获取最新提交的日期和作者（除去合并 dev 和 release 的提交）
        commit_date = subprocess.check_output(
            ['git', 'log', '-n', '1', '--skip', '2', '--format=%cd']
        ).decode('ascii').strip()
        commit_author = subprocess.check_output(
            ['git', 'log', '-n', '1', '--skip', '2', '--format=%an']
        ).decode('utf-8').strip()

        # 格式化提交日期
        commit_date = datetime.datetime.strptime(commit_date, '%a %b %d %H:%M:%S %Y %z')
        formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')

        return formatted_date, commit_author
    except Exception as e:
        log.warning(f"Error getting latest commit info: {str(e)}")
        return "Unknown", "Unknown"

def on_page_markdown(markdown, page, config, files):
    if page.meta:
        if 'hidden' in page.meta:
            page.meta['hide'] = copy.deepcopy(page.meta['hidden'])
            del page.meta['hidden']

    commit_date, commit_author = get_latest_commit_info()
    revision_note = f'\n\n---\n最后更新于{commit_date}'

    return f'{autocorrect.format(markdown)}{revision_note}'


    # release_date = f"\n\n---\n*发布于 {datetime.datetime.now().strftime('%Y-%m-%d')}，"
    # file_path = page.file.abs_src_path
    # last_modified = os.path.getmtime(file_path)
    # last_modified_date = datetime.datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d')
    # revision_note = f'最后更新于 {last_modified_date}*'
    # return f'{markdown}{release_date}{revision_note}'



