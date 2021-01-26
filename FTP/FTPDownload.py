import sys,io,ftplib,os

class FTPDownload:
    def __init__(self,host,username,password,localpath):
        self.host = host
        self.username = username
        self.password = password
        self.localpath = localpath
    def Download(self):
        ftp = ftplib.FTP(self.host)  # 实例化FTP对象
        ftp.login(self.username, self.password)  # 登录
        print(ftp.getwelcome())
        self.WalkDir(ftp,self.localpath)
        ftp.quit()



    def DownloadFile(self,ftp,curFile):
        savename = os.path.basename(curFile)
        bufsize = 1024  # 设置缓冲器大小
        fp = open(curFile, 'wb')
        ftp.retrbinary('RETR %s' % savename, fp.write, bufsize)
        fp.close()

    def WalkDir(self,ftp,curPath):
        if not os.path.isdir(curPath):
            os.makedirs(curPath)
        ftpcurdir = ftp.pwd()
        ftpflies = ftp.nlst()
        for ftpfile in ftpflies:
            sonPath = os.path.join(curPath,ftpfile)
            try:
                ftp.cwd(ftpfile)
                self.WalkDir(ftp,sonPath)
                ftp.cwd(ftpcurdir)
            except:
                self.DownloadFile(ftp,sonPath)
        

def main():
    #ftpload = FTPDownload("127.0.0.1","user","password","E:\Test1")
    ftpload = FTPDownload(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    ftpload.Download()

if __name__ == '__main__':
    main()