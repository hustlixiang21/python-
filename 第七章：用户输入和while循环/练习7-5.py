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
    