import mkdocs_gen_files
from datetime import datetime
import requests
from lxml import etree

filename = f"sample/福州大学宣讲会.md"

# Define the base URL
base_url = 'http://fjrclh.fzu.edu.cn/cms/xjh?page={}&flag=0&searchtext='
session = requests.session()
# Define the range of pages to iterate through
start_page = 1
end_page = 20

info = []

for page in range(start_page, end_page + 1):
    # Build the URL for the current page
    url = base_url.format(page)
    response = session.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        html = response.text
        root = etree.HTML(html)
        comp = root.xpath("//div[@class='xjhinfo']")
        addr_date = root.xpath("//span[@class='xjhtype']//span")

        for i in range(0, len(addr_date), 2):
            company = comp[i // 2].text.strip()
            address = addr_date[i].text.strip()
            date = addr_date[i + 1].text.strip()
            date_part, time_range = date.split(' ')
            start_time, end_time = time_range.split('-')

            # Parse date and time with the local timezone
            start_datetime = (datetime.strptime(date_part + ' ' + start_time, "%Y.%m.%d %H:%M"))
            end_datetime = (datetime.strptime(date_part + ' ' + end_time, "%Y.%m.%d %H:%M"))

            info.append({'公司': company, '地址': address, '日期': start_datetime, '开始时间': start_datetime, '结束时间': end_datetime})

    else:
        print(f"Failed to fetch page {page}. Status code: {response.status_code}")
        break  # 中止爬取
with mkdocs_gen_files.open(filename, "w") as f:
    print(f"---\ncomments: true\nhide:\n  - toc\n  - navigation\n---\n| 公司 | 地址 | 日期 |\n|----|----|----|", file=f)
    for detail in info:
        print(f"| {detail['公司']}  | {detail['地址']}  | {detail['日期']} |", file=f)

mkdocs_gen_files.set_edit_path(filename, "gen_pages.py")
