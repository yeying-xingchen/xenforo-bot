import requests
import json
import toml
#from . import plugin

# 从toml文件加载配置
config = toml.load('./config.toml')

key = config['auth']['key']
url = config['website']['url']
thread_id = config['listen']['thread_id']

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'XF-Api-Key': key
}

def get_message():
    payload = {'with_last_post': True}
    response = requests.get(url+"threads/"+thread_id, params=payload, headers = header)
    message = json.loads(response.text)
    return message['last_post']['message'],message['last_post']['username']

def send_message(user,message):
    payload = {'thread_id': thread_id,'message': "本消息由"+user+"请求，内容是：\n"+message}
    requests.post(url+"posts/",data=payload,headers=header)

message,user = get_message()
print(message)
send_message(user,"test")