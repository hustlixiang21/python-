class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """显示餐馆信息摘要概述。"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")


chinese_restanrant = Restaurant("Lixiang Restaurant", "Chinese Food")
chinese_restanrant.describe_restaurant()
korean_restaurant = Restaurant("Lishuo Restaurant","Korean Food")
korean_restaurant.describe_restaurant()
japanese_restanrant = Restaurant("Liqianjin Restaurant", "Japanese Food")
japanese_restanrant.describe_restaurant()