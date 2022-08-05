# coding=utf-8
guests = ['李翔', '王一芳', '李前进', '位艳丽', '李硕']
print("{},你来不了了，我要潇洒去了，哈哈哈!".format(guests.pop(4)))
print("{},你来不了了，我要潇洒去了，哈哈哈!".format(guests.pop(3)))
print("{},你来不了了，我要潇洒去了，哈哈哈!".format(guests.pop(2)))
print('{},我们俩潇洒去了，哈哈哈'.format(guests[1]))
del guests[1]
del guests[0]
print(guests)
# 删除列表函数有两个 del 直接删除，pop是弹出，里面的参数是索引值，还可以利用弹出的值，
# 还有一个remove参数是要删去的内容，然后跟pop一样，可以利用该值
