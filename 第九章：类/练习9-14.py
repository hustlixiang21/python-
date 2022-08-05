from random import choice
elements = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
for i in range(4):
    if choice(elements) == 4:
        print('Congratulations! You Win The Price!')
