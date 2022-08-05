def build_profile(first_name, last_name, **user_info):
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    return user_info


user_profile = build_profile(
    "xiang",
    "li",
    location="Wuhan",
    age=18,
    school="Huazhong University of Science and Technology",
)
print(user_profile)