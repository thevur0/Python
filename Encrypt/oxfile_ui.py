from tkinter import *
from tkinter.filedialog import askdirectory

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self._path1 = StringVar()
        self._path2 = StringVar()

        self.pack()
        self.window_init()
        self.createWidgets()

    def window_init(self):
        self.master.title('oxfile')
        self.master.bg = 'black'
        width, height = self.master.maxsize()[0]/5, self.master.maxsize()[1]/5


    def createWidgets(self):
        # fm1
        self.fm1 = Frame(self)
        self.folder1 = Entry(self.fm1, width='50', textvariable=self._path1)
        self.btnBrowse1 = Button(
            self.fm1, text="浏览", width='12', command=self.selectPath1)

        self.fm1.pack(side=TOP, expand=YES, fill='x', padx=10, pady=4)
        self.folder1.pack(side=LEFT, padx=5)
        self.btnBrowse1.pack(side=LEFT,padx=5)

        self.fm2 = Frame(self)
        self.folder2 = Entry(self.fm2, width='50', textvariable=self._path2)
        self.btnBrowse2 = Button(
            self.fm2, text="浏览", width='12', command=self.selectPath2)

        self.fm2.pack(side=TOP, expand=YES, fill='x', padx=10, pady=4)
        self.folder2.pack(side=LEFT, padx=5)
        self.btnBrowse2.pack(side=LEFT, padx=5)

        self.fm3 = Frame(self)
        self.btn = Button(self.fm3,text="转换")
        self.fm3.pack(side=TOP, expand=YES, fill='x', padx=10, pady=4)
        self.btn.pack(fill='x')

    

    def selectPath1(self):
        path = askdirectory()
        self._path1.set(path)

    def selectPath2(self):
        path = askdirectory()
        self._path2.set(path)
 

if __name__ == '__main__':
    app = Application()
    # to do
    app.mainloop()


