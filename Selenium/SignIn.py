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
                self.SendText(self.GetCtrl(item), item['text'])
            elif 'click'in item:
                self.SendClick(self.GetCtrl(item))
            elif 'sleep'in item:
                self.Sleep(item['sleep'])
    def GetCtrl(self,item):
        if 'id' in item:
            ctrl = self._browser.find_element_by_id(item['id'])
        if 'name' in item:
            ctrl = self._browser.find_element_by_name(item['name'])
        return ctrl
    
    #打开某个网址
    def OpenUrl(self,url):
        self._browser.get(url)

    def SendText(self,ctrl,text):
        
        try:
            if not ctrl.is_displayed():
                js = "document.getElementById(\"pwd_password\").style.display='block';"
                # 调用js脚本
                self._browser.execute_script(js)
                time.sleep(0.5)
            pass
        except expression as identifier:
            print("ctrl is None")
            pass

        ctrl.clear()
        ctrl.send_keys(text)

    def SendClick(self, ctrl):
        try:
            ctrl.click()
            pass
        except expression as identifier:
            print("ctrl is None")
            pass
        
    def Sleep(self,second):
        time.sleep(second)


def main():
    signin = SignIn(sys.argv[1])

if __name__ == "__main__":
    main()
    pass
