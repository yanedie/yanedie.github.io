---
comments: true
hide:
  - toc
created: 2023-09-18T00:57
updated: 2023-10-01T16:43
---
# 宣讲会

<link href="https://cdn.bootcdn.net/ajax/libs/datatables/1.10.21/css/jquery.dataTables.min.css" rel="stylesheet">
<script src="https://cdn.bootcdn.net/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script>
$(document).ready( function () { $('#myTable').DataTable(); } );
</script>

<table id="myTable" class="display" style="width:100%">
<thead>
<tr>
<th>公司</td>
<th>地点</td>
<th>日期</td>
<th>开始时间</td>
<th>结束时间</td>
</tr>
</thead>
<tbody>
{% for job in xjh() %}
<tr>
<td><a href="https://www.baidu.com/s?ie=UTF-8&wd={{ job.公司 }}" target="blank_new">{{ job.公司 }}</a></td>
<td>{{ job.地点 }}</td>
<td>{{ job.日期 }}</td>
<td>{{ job.开始时间 }}</td>
<td>{{ job.结束时间 }}</td>
</tr>
{% endfor %}
<tbody>
</table>

## 原理

写一个 python 爬虫，获取学校宣讲会网页的公司，地点和时间，函数返回字典。利用 macros 插件，将函数注册为宏，在 Markdown 中调用函数，即获得一个字典。因为 markdown 最终是渲染成 HTML，所以样式采取 jQuery 的 dataTables 方便筛选和搜索，结合 Jinja 的循环语法使用方括号[]运算符或者点语法取值。

=== "main.py"

    ```
    from datetime import datetime
    import requests
    from lxml import etree

    def define_env(env):
        @env.macro
        def xjh():
            base_url = 'http://fjrclh.fzu.edu.cn/cms/xjh?page={}&flag=0&searchtext='
            session = requests.session()
            # Define the range of pages to iterate through
            start_page = 1
            # 因为 分页由 JS 生成，而 requests 库只能获取 HTML 源代码，又不想用 bs4，所以分页手动赋值。
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

                        info.append({'公司': company, '地点': address, '开始时间': start_datetime, '结束时间': end_datetime})
                else:
                    print(f"Failed to fetch page {page}. Status code: {response.status_code}")
                    break  # 中止爬取
            return info
    ```

=== "Markdown"

    ```
    {% raw %}
    <link href="https://cdn.bootcdn.net/ajax/libs/datatables/1.10.21/css/jquery.dataTables.min.css" rel="stylesheet">
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <script>
    $(document).ready( function () { $('#myTable').DataTable(); } );
    </script>

    <table id="myTable" class="display" style="width:100%">
    <thead>
    <tr>
    <th>公司</td>
    <th>地点</td>
    <th>开始时间</td>
    <th>结束时间</td>
    </tr>
    </thead>
    <tbody>
    {% for job in xjh() %}
    <tr>
    <td>{{ job.公司 }}</td>
    <td>{{ job.地点 }}</td>
    <td>{{ job.开始时间 }}</td>
    <td>{{ job.结束时间 }}</td>
    </tr>
    {% endfor %}
    <tbody>
    </table>
    {% endraw %}
    ```

    !!! info "说明"

        `jquery.dataTables.js`为本地文件。如果引入链接，将会失效，我也不知道为什么。  
        总之，经过多次测试，这样才能正常渲染 dataTables。
