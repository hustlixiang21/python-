# coding=utf-8
first_name = "ada"
last_name = "lovelace"
full_name = '{} {}'.format(first_name, last_name)
# full_name = f"{first_name} {last_name}" 对于pythonversion>=3.6，f''字符串文本将起作用
print(full_name)
print('Hello,{}'.format(full_name.title()))
