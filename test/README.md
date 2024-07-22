写爬虫主要使用两个库
from bs4 import BeautifulSoup//解析网页
import requests//申请载入网页
其中封装了一个本地库url_manager用来管理url资源，防止循环爬取
可以学习如何攻克反爬措施

在写auto_search时使用了selenium库，可以模拟网页载入和鼠标点击、查找内容、输入内容的模拟
使用了内置的tkinter库用于弹窗提醒
其中要配置chormedriver的环境变量（本代码在chorme浏览器上实现）

在写微信自动发送消息的程序时使用了
import pyautogui
import pyperclip
其中第一个是用于自动化计算机行为的库，可以用来操作鼠标和键盘，模拟人类的输入方式，比如移动鼠标、点击按钮、输入文本等，在这里用于自动回复聊天机器人，还可以用于开发自动化工具
第二个用于操作粘贴板，可以通过pyperclip.copy('*')来向粘贴板中写入内容