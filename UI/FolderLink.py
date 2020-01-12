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


top = Tk()
top.title('目录链接')
#top.iconbitmap('.\\UI\\favicon.ico')



srcPath = StringVar()
desPath = StringVar()



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




def create_link(srcPath,desPath):
    if not os.path.isdir(srcPath) or not os.path.isdir(desPath):
        return

    dirname = os.path.basename(srcPath)
    desPath = os.path.join(desPath, dirname)

    cmdDelLink = 'rmdir {}'.format(desPath)
    os.system(cmdDelLink)
    cmdCreateLink = 'mklink /d {} {}'.format(desPath, srcPath)
    os.system(cmdCreateLink)
    pass


fm1 = Frame(top)


labelSrcPath = Label(fm1, text='链接目录:', justify=LEFT)
textEditSrc = Entry(fm1, textvariable=srcPath, justify=LEFT)
fm2 = Frame(top)
labelDesPath = Label(fm2, text='目标目录:', justify=LEFT)
textEditDes = Entry(fm2, textvariable=desPath, justify=LEFT)

fm3 = Frame(top)

def onBtnLink():
    create_link(srcPath.get(), desPath.get())
    pass
btnLink = Button(fm3, text="关联", command=onBtnLink)

fm1.pack(side=TOP, fill=X, expand=YES, padx=5)
labelSrcPath.pack(side=LEFT)

textEditSrc.pack(side=LEFT, fill=BOTH, padx=5)

fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)
labelDesPath.pack(side=LEFT)
textEditDes.pack(side=LEFT, fill=BOTH, padx=5)
fm3.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)
btnLink.pack(side=TOP, fill=BOTH, padx=5)


top.mainloop()
