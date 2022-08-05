# coding=utf-8
favorite_places = {
    "李翔": ["西安", "武汉", "北京"],
    "李硕": ["新疆", "西藏", "内蒙古"],
    "王屁芳": ["上海", "庐山", "华山"],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:") 
    for place in places:
        print(f"- {place.title()}")