root_url="https://www.doggystyles.net/xs/fkmg/"

from bs4 import BeautifulSoup
import requests
from url_manager import URLmanager
urls=URLmanager()
import re
urls.add_new_url(root_url)
fout=open("test/url.txt","w",encoding="utf-8")
url=urls.get_url()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
r=requests.get(url,timeout=3,headers=headers)
html_doc=r.text
soup=BeautifulSoup(html_doc,"html.parser")
div_node=soup.find("ul",id="newlist")
div_node1=div_node.find_all("li")
for link in div_node1:
    herf="https://www.doggystyles.net"+link.a["href"]
    urls.add_new_url(herf)
    print(herf)
    url=urls.get_url()
    r=requests.get(url,timeout=3,headers=headers)
    html_doc=r.content
    soup1=BeautifulSoup(html_doc,"html.parser")
    s1=soup1.find("div",class_="panel-heading")
    title=s1.get_text()
    if re.match(r"\d+.\S+",title):
        fout.write("%s\n"%(title))
        print(title)
    div_node11=soup1.find_all("p")
    for link in div_node11:
        if link.get_text()=="更多内容加载中...请稍候...":
            break
        fout.write("%s\n"%(link.get_text()))
