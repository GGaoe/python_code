from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import messagebox
import os

def show_popup(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("今日晚霞预测", message) 
    #root.destroy()
data=""
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
service = Service('C:/Users/高歌/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
# 初始化浏览器
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.get('https://www.sunsetbot.top/')

select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'selector_large')))  

select = Select(select_element)
select.select_by_visible_text('今天日落')
time.sleep(0.5)

we=driver.find_element(By.XPATH, "//input[@id='city_input']")
#print(we.text)
we.send_keys("南京")
time.sleep(0.5)
we1=driver.find_element(By.ID, "srch_btn")
#print(we1.text)
we1.click()
time.sleep(1)
we2=driver.find_element(By.ID, "tb_event_time")
#print(we2.text)
data="今日日落时间:"+we2.text+"\n"
time.sleep(0.5)
we3=driver.find_element(By.ID, "tb_quality")
data+="今日晚霞质量:"+we3.text+"\n"
#print(we3.text)
data+="晚霞质量参考:"+"\n"+"- 0.001-0.05:微微烧，或者火烧云云况不典型没有预报出来；"+"\n"
data+="- 0.05-0.2:小烧，大气很通透的情况下才会比较好看；"+"\n"
data+="- 0.2-0.4:小烧到中等烧；"+"\n"
data+="- 0.4-0.6:中等烧，比较值得看的火烧云；"+"\n"
data+="- 0.6-0.8:中等烧到大烧程度的火烧云；"+"\n"
data+="- 0.8~1.0:不是很完美的大烧火烧云，例如云量没有最高、大气偏污、持续时间偏短、有低云遮挡等；"+"\n"
data+="- 1.0~1.5:典型的火烧云大烧；"

with open("C:/Users/高歌/Desktop/晚霞预测结果.txt","w",encoding="utf-8") as file:
    file.write(data)

driver.quit()
show_popup(f"查询结果:\n{data}")
