# coding=utf-8
pets = []
pet = {"type": "dog", "owner": "李翔"}
pets.append(pet)
pet = {"type": "cat", "owner": "王一芳"}
pets.append(pet)
pet = {"type": "cat", "owner": "李向前"}
pets.append(pet)
for pet in pets:
    print(f"It's a {pet['type']}.The owner's name is {pet['owner']}!")
