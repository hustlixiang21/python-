class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        msg = f"{self.first_name} {self.last_name} is {self.age} years old."
        print(msg)

    def greet_user(self):
        msg = f"Welcome to our website,{self.first_name} {self.last_name}"
        print(msg)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = []

    def show_privileges(self):
        print(
            f"Dear Admin {self.first_name} {self.last_name},you have the following privileges:"
        )
        for privilege in self.privileges:
            print(f"- {privilege}")


Li_Xiang = Admin("Xiang", "Li", 18)
Li_Xiang.privileges = ["can add post", "can delete post", "can ban user"]
Li_Xiang.describe_user()
Li_Xiang.show_privileges()
