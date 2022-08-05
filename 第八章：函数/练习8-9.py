from pyexpat.errors import messages


def show_message(messages):
    for message in messages:
        print(message)


messages = ['hello','hi','yyds']
show_message(messages)
