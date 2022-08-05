# coding=utf-8
guests = ['王一芳', '李前进', '位艳丽', '李硕']
guests.insert(0, '李翔')
guests.insert(3, '李新长')
guests.append('白秀荣')
print('{},my love,please have a dinner with me!'.format(guests[1]))
print('{},{},{},{},跟我一起吃晚饭吧，哈哈哈!'.format(
    guests[2], guests[3], guests[4], guests[5]))
# 列表增加函数有 insert（）和append（）
# 对于insert（），两个参数前面的是索引，后面写插入的内容，
# append（）括号内直接是插入的内容，并且是在列表最后
