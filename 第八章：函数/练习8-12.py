def make_sandwich(*toppings):
    for topping in toppings:
        print(f'-{topping}')
    print('\n')

make_sandwich('mushrooms')
make_sandwich('green peppers','mushrooms')
make_sandwich('extra cheese','green peppers','mushrooms')