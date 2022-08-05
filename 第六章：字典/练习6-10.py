# coding=utf-8
favorite_numbers = {
    '李翔':[1,2,3],
    '李硕':[4,5,6],
    '王屁芳':[7,8,9],
}
for name,numbers in favorite_numbers.items():
    print(f"{name}最喜欢的数字是:")
    for number in numbers:
        print(number)
