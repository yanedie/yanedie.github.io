import os
import re

def process_markdown_file(md_path):
    # 获取目录名和挑战编号
    dir_name = os.path.basename(os.path.dirname(md_path))
    match = re.search(r'coding-challenge-(\d+)\.md$', md_path)
    if not match:
        return
    
    challenge_num = match.group(1)
    
    # 创建对应的JS文件
    js_dir = os.path.dirname(md_path)
    js_filename = f'challenge-{challenge_num}.js'
    js_path = os.path.join(js_dir, js_filename)
    
    # 如果JS文件不存在，创建空文件
    if not os.path.exists(js_path):
        with open(js_path, 'w', encoding='utf-8') as f:
            pass
    
    # 读取markdown文件内容
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经包含了 example 部分
    if '??? example' in content:
        return
    
    # 构建要插入的内容
    relative_path = f'docs/code/javascript/the-complete-javascript-course/coding-challenges/{dir_name}/challenge-{challenge_num}.js'
    insert_content = f'''---

```javascript
--8<-- "{relative_path}"
    ```'''
    
    # 在 "GOOD LUCK 😀" 后插入内容
    if '**GOOD LUCK 😀**' in content:
        parts = content.split('**GOOD LUCK 😀**')
        new_content = parts[0] + '**GOOD LUCK 😀**\n' + insert_content
        if len(parts) > 1:
            new_content += parts[1]
            
        # 写回文件
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

def main():
    # 设置基础路径
    base_path = r'd:\Blog\docs\code\javascript\the-complete-javascript-course\coding-challenges'
    
    # 遍历所有子目录
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.startswith('coding-challenge-') and file.endswith('.md'):
                md_path = os.path.join(root, file)
                process_markdown_file(md_path)

if __name__ == '__main__':
    main()