from bs4 import BeautifulSoup
import requests
import re

url="http://www.crazyant.net/"
r=requests.get(url)
if r.status_code!=200:
    raise Exception("Failed to open the url")
html_doc=r.content

soup=BeautifulSoup(html_doc,"html.parser")
div_node=soup.find_all("h2",class_="entry-title")
#print(div_node)
for node in div_node:
    #soup1=BeautifulSoup(node,"html.parser")
    s=node.find_all("a")
    #for s1 in s:
        #print(s1["href"],s1.get_text(),"\n")
#for link in div_node:
#    print(link.name,link.a["href"],link.get_text(),"\n")