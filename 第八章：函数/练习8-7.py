# coding=utf-8
def make_album(singer, album_name, number=None):
    album = {"singer": singer, ";album": album_name}
    if number:
        album["number"] = number
    return album


print(make_album("周杰伦", "我很忙"))
print(make_album("王力宏", "十八般武艺"))
print(make_album("周杰伦", "叶惠美"))
