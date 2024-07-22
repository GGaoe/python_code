from bs4 import BeautifulSoup
import requests
#with open("test/text.html",encoding="utf-8") as fin:
#    html_doc = fin.read()

url="https://ggaoe.top/archives"
html_doc=requests.get(url).content
soup=BeautifulSoup(html_doc,"html.parser")
div_node=soup.find_all("a",class_="archive-article-title")

#links = div_node.find_all("a")
#for link in div_node:
    #print(link.name,link["href"],link.get_text(),"\n")
    #print(link.name,link["href"],link.get_text(),"\n")
