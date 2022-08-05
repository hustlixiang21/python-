# coding=utf-8
guests = ['王一芳','李前进', '位艳丽', '李硕']
print('{},my love,please have a dinner with me!'.format(guests[0]))
print('{},{},{},跟我一起吃晚饭吧，哈哈哈!'.format(guests[1],guests[2],guests[3]))
print('{}在打游戏，来不了了！'.format(guests[3]))
guests.remove('李硕')
guests.insert(3,'李翔')
print('{},my love,please have a dinner with me!'.format(guests[0]))
print('{},{},{},跟我一起吃晚饭吧，哈哈哈!'.format(guests[1],guests[2],guests[3]))