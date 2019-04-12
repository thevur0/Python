from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import keyword
import json
import os
import sys

class SignIn:

    def __init__(self,jsonfile):

        f = open(jsonfile, 'r')
        strJson = f.read()
        self._jsondata = json.loads(strJson)
        #初始化浏览器
        self._browser = webdriver.Chrome()
        self.RunJson()

    def RunJson(self):
        for item in self._jsondata:
            if 'url' in item:
                self.OpenUrl(item['url'])
            elif 'text' in item:
                self.SendText(item['id'], item['text'])
            elif 'click'in item:
                self.SendClick(item['id'])
            elif 'sleep'in item:
                self.Sleep(item['sleep'])
        
    #打开某个网址
    def OpenUrl(self,url):
        self._browser.get(url)

    def SendText(self,id,text):
        ctrl = self._browser.find_element_by_id(id)
        #if not ctrl：
           # return

        if not ctrl.is_displayed():
            js = "document.getElementById(\"pwd_password\").style.display='block';"
            # 调用js脚本
            self._browser.execute_script(js)
            time.sleep(0.5)

        ctrl.clear()
        ctrl.send_keys(text)

    def SendClick(self, id):
        ctrl = self._browser.find_element_by_id(id)
        #if not ctrl：
            #return
        ctrl.click()

    def Sleep(self,second):
        time.sleep(second)


def main():
    signin = SignIn(sys.argv[1])

if __name__ == "__main__":
    main()
    pass
