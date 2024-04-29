import main

def command(message,user):
    if message == "help":
        help = '''总菜单 | 机器人小K
==================
help | 展示总菜单
jrrp | 获取今日人品值
ping | Ping网站
about | 关于信息
======================
机器人小K 3.0.0 alpha-3'''
        main.send_message(user,help)