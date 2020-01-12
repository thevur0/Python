import os
import sys
import threading

class LuacThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

class Luac:
    listLuac = {}
    def __init__(self,luaPath,luacPath):
        if not os.path.exists(luacPath):
            os.makedirs(luacPath)
        
        for root, dirs, files in os.walk(luaPath):
            for luafile in files:
                ext = os.path.splitext(luafile)[1]
                if ext == '.lua' or ext == '.bytes':
                    fullPath = os.path.join(root,luafile)
                    luacName = fullPath.replace(luaPath+'\\','').replace('\\','.')
                    print(os.path.join(luacPath,luacName))
                    self.listLuac[fullPath]=luacName
        
        try:
            for i in range(0,10)：
                LuacThread
        except:
            print ("Error: 无法启动线程")

            def GenLuac(self,luaPath,luacPath):
                pass


if __name__ == "__main__":
    luac = Luac(sys.argv[1],sys.argv[2])
    pass