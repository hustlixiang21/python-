# coding=utf-8
def make_album(singer, album_name, number=None):
    album = {"singer": singer, ";album": album_name}
    if number:
        album["number"] = number
    return album


while True:
    print("Please enter the album's name and composer!")
    print("(Enter 'quit' to end the process!)")
    singer = input("Album's composer:")
    if singer == "quit":
        break
    album_name = input("Album's name:")
    if album_name == "quit":
        break
    print(make_album(singer, album_name))
    print("\n")
