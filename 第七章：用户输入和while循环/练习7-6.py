"""
while True:
    message=input("How old are you?\n")
    if message == 'quit':
        break
    age=int(message)
    if age<3:
        print("You are free of charge!\n")
    elif age<=12:
        print("You ought to pay 10$\n")
    else:
        print("You ought to pay 15$\n")
    使用break结束while循环
"""
'''
message = ""
message = input("How old are you?\n")
while message != 'quit':
    age = int(message)
    if age < 3:
        print("You are free of charge!\n")
    elif age <= 12:
        print("You ought to pay 10$\n")
    else:
        print("You ought to pay 15$\n")
    message = input("How old are you?\n")
    使用条件判断
'''
active = True
while active:
    message=input("How old are you?\n")
    if message == 'quit':
        active = False
    else:
        age=int(message)
        if age<3:
            print("You are free of charge!\n")
        elif age<=12:
            print("You ought to pay 10$\n")
        else:
            print("You ought to pay 15$\n")