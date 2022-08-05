from uer import User

class Privileges:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("Dear Admin,you have the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.Privilege = Privileges()