from tkinter import *
top = Tk()

li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(top)
listb2 = Listbox(top)
for item in li:
    listb.insert(0,item)
 
for item in movie:
    listb2.insert(0,item)
 
listb.pack()
listb2.pack()

# 进入消息循环
top.mainloop()