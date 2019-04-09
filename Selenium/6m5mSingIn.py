from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import keyword

url = 'http://www.6m5m.com/login.html'
#初始化浏览器
browser = webdriver.Chrome()
#打开某个网址
browser.get(url)

#verfile = open("C:/Test.txt", 'w', encoding="utf-8")
#verfile.write(browser.page_source)
#verfile.close()

browser.find_element_by_xpath("//*[@id='txt_account']").clear()  # 清空输入框
browser.find_element_by_xpath("//*[@id='txt_account']").send_keys("thevur")  # 输入账号
time.sleep(1)
#pwtextctrl1 = browser.find_element_by_id('txt_password')
pwtextctrl2 = browser.find_element_by_id('pwd_password')

if pwtextctrl2.is_displayed():
    pwtextctrl2.clear()
    pwtextctrl2.send_keys('Lhy123456')
else:
    js = "document.getElementById(\"pwd_password\").style.display='block';"
    # 调用js脚本
    browser.execute_script(js)
    time.sleep(1)
    pwtextctrl2.clear()
    pwtextctrl2.send_keys('Lhy123456')
time.sleep(1)
browser.find_element_by_xpath("//*[@id='user_login_btn']").click()  # 登录

url = 'http://www.6m5m.com/index.php'
browser.get(url)
browser.find_element_by_id('add_follow_').click() #签到
