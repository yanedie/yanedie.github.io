---
<%*
let title = tp.file.title;
if (title.includes("未命名")) {
    let newTitle = tp.file.creation_date("YYYY-MM-DD");
    await tp.file.rename(newTitle);
}
-%>
authors:
  - yanedie
date: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# <% tp.file.creation_date("YYYY-MM-DD") %>
