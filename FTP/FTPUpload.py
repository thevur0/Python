import sys,io,ftplib,os

class FTPUpload:
    def __init__(self,host,username,password,localpath):
        self.host = host
        self.username = username
        self.password = password
        self.localpath = localpath

    def Upload(self):
        ftp = ftplib.FTP(self.host)  # 实例化FTP对象
        ftp.login(self.username, self.password)  # 登录
        print(ftp.getwelcome())

        filelist = os.listdir(self.localpath)
        for onefile in filelist:
            self.WalkDir(ftp,os.path.join(self.localpath,onefile))

        ftp.quit()

    def WalkDir(self,ftp,curPath):
        if os.path.isfile(curPath):
            self.UploadFile(ftp,curPath)
        elif os.path.isdir(curPath):
            dirname = os.path.basename(curPath)
            ftpcurdir = ftp.pwd()
            try:
                ftp.mkd(dirname)
            except:
                1
            finally:
                ftp.cwd(dirname)
                filelist = os.listdir(curPath)
                for onefile in filelist:
                    self.WalkDir(ftp,os.path.join(curPath,onefile))
                ftp.cwd(ftpcurdir)    
            

    def UploadFile(self,ftp,curFile):

        basename = os.path.basename(curFile)
        ftpflies = ftp.nlst()
        savename = basename
        i = 0
        while savename in ftpflies:
            i+=1
            savename = basename + str(i)
            
        bufsize = 1024  # 设置缓冲器大小
        fp = open(curFile, 'rb')
        ftp.storbinary('STOR ' + savename, fp, bufsize)
        fp.close()
        

def main():
    #ftpload = FTPUpload("127.0.0.1","user","password","E:\Test")
    ftpload = FTPUpload(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    ftpload.Upload()

if __name__ == '__main__':
    main()