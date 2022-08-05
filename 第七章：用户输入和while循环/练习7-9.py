sandwich_orders = ["veggie", "pastrami", "grilled cheese","pastrami","turkey", "pastrami","roast beef"]
print('The pastrami has been sold out!')
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)
