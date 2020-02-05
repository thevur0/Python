import os,sys
import shutil
class DeleteFile:
    deleteFileList = ["Assets/Output.txt",
    "Assets/XLua/*.xml"]
    def __init__(self,root):
        for item in self.deleteFileList:
            fullname = os.path.join(root,item)
            filename = os.path.basename(fullname)

            if filename.find('*')>=0:
                filedir = os.path.dirname(fullname)
                for root,dirs,files in os.walk(filedir):
                    for onefile in files:
                        if onefile.lower().find(filename.replace('*',"").lower())>=0:
                            os.remove(os.path.join(root,onefile))
                    
            elif os.path.exists(fullname):
                if os.path.isdir(fullname):
                    shutil.rmtree(fullname)
                else:
                    os.remove(fullname)
        pass
    pass

if __name__ == "__main__":
    deletefile = DeleteFile(sys.argv[1])
    pass