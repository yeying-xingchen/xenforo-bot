import main

def command(message,user):
    if message == "help":
        help = '''这是一条帮助信息'''
        main.send_message(user,help)
    else:
        main.send_message(user,"收到消息："+message)