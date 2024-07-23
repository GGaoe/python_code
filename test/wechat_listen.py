from wxauto import *
import requests
from urllib import request, parse
import time
import json

# python3
# Please install OpenAI SDK first：`pip3 install openai`
from openai import OpenAI

client = OpenAI(api_key="sk-a707aa3c7d5d4916bc57bb65acaed7b0", base_url="https://api.deepseek.com/v1")


wx=WeChat()
# 给文件传输助手发送消息
#wx.SendMsg('这是通过wxauto发给你的消息！', '文件传输助手')

listen_list = [
    #'16',
    #'🐶🐶🐶😋'
    '好🍉一起吃'
    #'小号'
]

for i in listen_list:
    wx.AddListenChat(who=i, savepic=False)

    # 持续监听消息，并且收到消息后回复“收到”
wait = 1  # 设置1秒查看一次是否有新消息
while True:
    newfriends = wx.GetNewFriends()
    if  not newfriends:
        pass
    else:
        print('有新好友请求...')
        for friend in newfriends:
            remark = f'备注{friend.name}'
            friend.Accept(remark=remark)  # 接受好友请求，并设置备注和标签
            wx.AddListenChat(who=remark, savepic=False)
    print('正在监听消息...')
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who              # 获取聊天窗口名（人或群名）
        one_msgs = msgs.get(chat)   # 获取消息内容
        for msg in one_msgs:
            msgtype = msg.type       # 获取消息类型
            content = msg.content    # 获取消息内容，字符串类型的消息内容
            #print(f'【{who}】：{content}')
            if "@GPT" in content:
        # ===================================================
        # 处理消息逻辑（如果有）
        # 
        # 处理消息内容的逻辑每个人都不同，按自己想法写就好了，这里不写了
        # 
        # ===================================================
        
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": "你现在是一只可爱的猫娘，请在每一句回答后发送喵进和一个emoji表情包"},
                        {"role": "user", "content": content},
                    ],
                    stream=False
                )
                msg=response.choices[0].message.content
                # 如果是好友发来的消息（即非系统消息等），则回复收到
                if msgtype == 'friend':
                    chat.SendMsg(msg=msg)  # 回复收到
    time.sleep(wait)
