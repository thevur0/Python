import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import io,sys,os
import configparser
import subprocess
import time



def run_cmd(cmd):
    # Popen call wrapper.return (code, stdout, stderr)
    child = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True)
    out, err = child.communicate()
    ret = child.wait()
    return (ret, out, err)


(ret, out, err) = run_cmd('svn')

top = Tk()
top.title('文件链接')
#top.iconbitmap('.\\UI\\favicon.ico')

srcPath = '..\\..\\work3d\\scenes'
desPath = '..\\assets\\work3d\\scenes'

srcPath = os.path.join(os.path.abspath(os.curdir), srcPath)
desPath = os.path.join(os.path.abspath(os.curdir), desPath)

svnEnable = False

try:
    if str(err, encoding="utf-8").find('svn help') != -1:
        svnEnable = True
        pass
except:
    pass

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
    tkinter.messagebox.showerror('错误', '{}不存在\n请使用flcfg.ini指认目录\n[Config]\nSrcPath=Work3d/Scenes\nDesPath=Assets/Work3d/Scenes'.format(srcPath))


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
        fileList = os.listdir(srcPath)
        for item in fileList:
            if os.path.isdir(os.path.join(srcPath,item)):
                listDir.append(item)
#    for root, dirs, files in os.walk(srcPath):
#        if len(dirs)>0 :
#            listDir = dirs
#        pass

    return listDir

def create_link(srcPath,desPath):
    if not os.path.isdir(srcPath):
        return

    cmdDelLink = 'rmdir {}'.format(desPath)
    os.system(cmdDelLink)
    cmdCreateLink = 'mklink /d {} {}'.format(desPath, srcPath)
    os.system(cmdCreateLink)
    pass


fm1 = Frame(top)
labelPath = Label(fm1, text='SVN:  {}\nAsset: {}'.format(
    os.path.realpath(srcPath), os.path.realpath(desPath)), justify=LEFT)


fm2 = Frame(top)
btnUpdateAll = Button(fm2, text="更新全部", command=update_all)
if not svnEnable:
    btnUpdateAll.configure(state='disabled')


def onBtnLinkAll():
    paths = get_son_path(srcPath)
    for p in paths:
        create_link(os.path.join(srcPath, p),
                    os.path.join(desPath, p))
    pass


btnLinkAll = Button(fm2, text="关联全部", command=onBtnLinkAll)

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
if not svnEnable:
    btnUpdate.configure(state='disabled')

def onBtnLink():
    create_link(os.path.join(srcPath, xVariable.get()),
                os.path.join(desPath, xVariable.get()))
    pass




btnLink = Button(fm3, text="关联", command=onBtnLink)

fm1.pack(side=TOP, fill=X, expand=YES, padx=5)
labelPath.pack(side=LEFT, fill=X, expand=YES)



fm3.pack(side=TOP, fill=X, expand=YES, padx=5, pady=5)
sonPathList.pack(side=LEFT,fill = X)

btnLink.pack(side=RIGHT, padx=5)
btnUpdate.pack(side=RIGHT)

fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)
btnUpdateAll.pack(side=TOP, fill=BOTH)
btnLinkAll.pack(side=TOP, fill=BOTH)

top.mainloop()
