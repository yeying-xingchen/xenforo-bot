import requests
import toml
import json
import plugin
import time

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
    payload = {'thread_id': thread_id,'message': message+"\n本消息由"+user+"请求。"}
    requests.post(url+"posts/",data=payload,headers=header)

if __name__ == "__main__":
    while True:
        message,user = get_message()
        print(message)
        plugin.command(message,user)
        time.sleep(20)