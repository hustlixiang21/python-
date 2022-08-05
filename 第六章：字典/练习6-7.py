person1 = {"first_name": "xiang", "last_name": "li", "age": "18", "city": "wuhan"}
person2 = {"first_name": "yifang", "last_name": "wang", "age": "18", "city": "wuhan"}
person3 = {"first_name": "shuo", "last_name": "li", "age": "16", "city": "wuhan"}
personal_information = [person1,person2,person3]
for every_person in personal_information:
    print(f"information:")
    for key,value in every_person.items():
        print(f"{key}:{value}")
    print('\n')
