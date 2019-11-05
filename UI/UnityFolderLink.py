import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import io,sys,os
import configparser

top = Tk()
top.title('文件链接')
#top.iconbitmap('.\\favicon.ico')

srcPath = '..\\work3d\scenes'
desPath = 'assets\\work3d'

srcPath = os.path.join(os.path.abspath(os.curdir), srcPath)
desPath = os.path.join(os.path.abspath(os.curdir), desPath)

def load_ini(flConfig):

    global srcPath
    global desPath
    config = configparser.ConfigParser()
    config.readfp(open(flConfig))

    src = config.get("Config", "SrcPath")
    des = config.get("Config", "DesPath")

    if os.path.isdir(src):
        srcPath = src
    if os.path.isdir(des):
        desPath = des
    pass
try:
    load_ini('flcfg.ini')
except:
    pass

if not os.path.isdir(srcPath):
    tkinter.messagebox.showerror('错误','{}不存在'.format(srcPath))


def update_all():
    if os.path.exists(srcPath):
        cmdRevrt = 'svn revert {}'.format(srcPath)
        os.system(cmdRevrt)
        cmdUpdate = 'svn update {}'.format(srcPath)
        os.system(cmdUpdate)
    pass

def update_path(dealWithpath):
    dealWithpath = os.path.join(srcPath,dealWithpath)
    if os.path.exists(dealWithpath):
        cmdRevrt = 'svn revert -R {}'.format(dealWithpath)
        os.system(cmdRevrt)
        cmdUpdate = 'svn update {}'.format(dealWithpath)
        os.system(cmdUpdate)
    pass



def get_son_path(srcPath):
    listDir = []
    if os.path.isdir(srcPath):
        listDir = os.listdir(srcPath)
#    for root, dirs, files in os.walk(srcPath):
#        if len(dirs)>0 :
#            listDir = dirs
#        pass

    return listDir

def create_link(srcPath,desPath):
    cmdDelLink = 'rmdir {}'.format(desPath)
    os.system(cmdDelLink)
    cmdCreateLink = 'mklink /d {} {}'.format(desPath, srcPath)
    os.system(cmdCreateLink)
    pass


fm1 = Frame(top)
labelPath = Label( fm1, text='SVN:  {}\nAsset: {}'.format(srcPath, desPath), justify=LEFT)


fm2 = Frame(top)
btnUpdateAll = Button(fm2, text="更新全部", command=update_all)

fm3 = Frame(top)
xVariable = tkinter.StringVar()
sonPathList = tkinter.ttk.Combobox(fm3, textvariable=xVariable)
sonPathList.config(state='readonly')

sonPathList['values'] = get_son_path(srcPath)
if len(sonPathList['values']) > 0:
    sonPathList.current(0)

def onBtnUpdate():
    update_path(os.path.join(srcPath, xVariable.get()))
    pass


btnUpdate = Button(fm3, text="更新", command=onBtnUpdate)

def onBtnLink():
    create_link(os.path.join(srcPath, xVariable.get()),
                os.path.join(desPath, xVariable.get()))
    pass


btnLink = Button(fm3, text="关联", command=onBtnLink)

fm1.pack(side=TOP, fill=X, expand=YES, padx=5)
labelPath.pack(side=LEFT, fill=X, expand=YES)



fm3.pack(side=TOP, fill=X, expand=YES, padx=5, pady=5)
sonPathList.pack(side=LEFT)
btnUpdate.pack(side=LEFT, padx=5)
btnLink.pack(side=LEFT)

fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)
btnUpdateAll.pack(side=TOP, fill=BOTH)
top.mainloop()
