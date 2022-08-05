users = []# write some users' name
if users:
    for user in users:
        if user == 'admin':
            print("Hello {},would you like to see a status report?".format(user))
        else:
            print("Hello {},thank you for logging again!".format(user))
else:
    print("We need to find some users!")