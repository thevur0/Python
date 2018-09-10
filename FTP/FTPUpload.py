import sys,io,ftplib

class SVNUpload:
    def __init__(self,host,user,password,localpath):
        self.host = host
        self.user = user
        self.password = password
        self.localpath = localpath
    def Upload():
        f = ftplib.FTP(host)  # 实例化FTP对象
        f.login(username, password)  # 登录
        pwd_path = f.pwd()
        print("FTP当前路径:", pwd_path)

    def ftp_upload():
        #'''以二进制形式上传文件'''
        file_remote = 'ftp_upload.txt'
        file_local = 'D:\\test_data\\ftp_upload.txt'
        bufsize = 1024  # 设置缓冲器大小
        fp = open(file_local, 'rb')
        f.storbinary('STOR ' + file_remote, fp, bufsize)
        fp.close()

def main():
    svnload = SVNUpload("127.0.0.1:21","test","test123",)
    svnload.Upload()

if __name__ == '__main__':
    main()