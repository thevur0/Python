import sys,io,os

class PMP2:
    def __init__(self,file1,file2):
        self.file1 = file1
        self.file2 = file2

    def Trans(self):
        
        fp1 = open(self.file1, 'r',encoding='UTF-8')
        strSave = ''
        str1 = fp1.read()
        head = 0
        for i in range(1,200):
            trail = str1.find(str(i+1)+".",head)
            str2 = self.TranAnswer(str1[head:trail])
            strSave = strSave.join(str2)
            head = trail


    def TranAnswer(self,strAnswer):
        head = 0
        str1 = ""
        for j in range(0,3):
            head = strAnswer.find(chr(j+ord('A')) +".",head)
            trail = strAnswer.find("\n",head)
            str2 = strAnswer[head:trail]
            str1 = str1.join(str2)
        return str1

        

def main():
    pmp = PMP2(sys.argv[1],sys.argv[2])
    pmp.Trans()

if __name__ == '__main__':
    main()