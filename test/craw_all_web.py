from bs4 import BeautifulSoup
import requests
from url_manager import URLmanager
root_url="https://ggaoe.top/archives"
urls=URLmanager()
urls.add_new_url(root_url)
fout=open("test/url.txt","w",encoding="utf-8")
while urls.has_new_url():
    url=urls.get_url()
    r=requests.get(url,timeout=3)
    html_doc=r.content
    soup=BeautifulSoup(html_doc,"html.parser")
    title=soup.title.string
    fout.write("%s\t%s\n"%(url,title))
    div_node=soup.find_all("a",class_="archive-article-title")
    for link in div_node:
        herf="https://ggaoe.top/"+link["href"]
        urls.add_new_url(herf)
    div_node1=soup.find_all("a",class_="extend next")
    for link in div_node1:
        herf="https://ggaoe.top/"+link["href"]
        urls.add_new_url(herf)