from admin import Admin

Li_Xiang = Admin("Xiang", "Li", 18)
Li_Xiang.Privilege.privileges = ["can add post", "can delete post", "can ban user"]
Li_Xiang.describe_user()
Li_Xiang.Privilege.show_privileges()
