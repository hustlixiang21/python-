class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        msg = f"{self.first_name} {self.last_name} is {self.age} years old."
        print(msg)

    def greet_user(self):
        msg = f"Welcome to our website,{self.first_name} {self.last_name}"
        print(msg)


user1 = User('Xiang','Li',18)
user1.describe_user()
user1.greet_user()
user2 = User('Yifang','Wang',18)
user2.describe_user()
user2.greet_user()