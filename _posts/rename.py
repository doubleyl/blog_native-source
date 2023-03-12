import os
import re

def process_directory(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            # 如果是子目录，则递归处理子目录中的文件
            process_directory(filepath)
        elif filename.endswith('.md'):
            # 如果是Markdown文件，则修改前两行标题
            with open(filepath, 'r+', encoding='utf-8') as f:
                # 读取前两行内容
                line1 = f.readline()
                line2 = f.readline()

                # 使用正则表达式匹配第二行标题中的中文或英文名字
                pattern = re.compile(r'^(title:\s*)(.*)', re.MULTILINE)
                match = pattern.search(line2)
                if match:
                    title = match.group(2)
                    # 将中文或英文名字替换为当前文件的文件名
                    new_title = filename[:-3]
                    new_line2 = line2.replace(title, new_title)

                    # 将修改后的前两行内容写回文件
                    f.seek(0)
                    f.write(line1)
                    f.write(new_line2)
                    f.seek(0, 2)
                    # f.truncate()
                    f.close()

# 指定目录路径并开始递归处理
directory = './' # 更改为实际的目录路径
process_directory(directory)
