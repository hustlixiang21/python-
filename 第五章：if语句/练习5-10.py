users_names = ['lixiang', 'lishuo', 'liqianjin', 'weiyanli', 'wangyifang']
new_users_names = ['lixiang', 'ruancong',
                   'majunhang', 'zhangyuyang', 'wenxinyu']
for new_users_name in new_users_names:
    flag=0
    for users_name in users_names:
        if users_name.lower() == new_users_name.lower():
            flag=1
    if flag:
        print("{} has been used!".format(new_users_name.title()))
    else:
        print("{} hasn't been used!".format(new_users_name.title()))
