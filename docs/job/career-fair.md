---
title: 福州大学宣讲会
comments: true
hide:
    - toc
    - navigation
    - footer
---

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

<script type="text/javascript" charset="utf8" src="https://cdn.bootcdn.net/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script>
$(document).ready( function () { $('#myTable').DataTable(); } );
</script>