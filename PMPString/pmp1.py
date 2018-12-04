import sys,io,os

class PMP1:
    def __init__(self,file1,file2):
        self.file1 = file1
        self.file2 = file2
        self.sign1 = '、'
        self.sign2 = '，'

    def Find(self,strFind,sign,index=0):
        pos = strFind.find(sign+self.sign1,index)
        if pos < 0:
            pos = strFind.find(sign+self.sign2,index)
        return pos

    def Trans(self):
        
        fpRead = open(self.file1, 'r',encoding='UTF-8')
        fpWrite = open(self.file2, 'w',encoding='UTF-8')
        #strSave = ''
        str1 = fpRead.read()
        head = 0
        for i in range(1,200):
            trail = self.Find(str1,str(i+1),head) 
            str2 = self.TranQuestion(i,str1[head:trail])
            fpWrite.writelines(str2)
            head = trail

        str2 = self.TranQuestion(200,str1[trail:])
        fpWrite.writelines(str2)
        fpRead.close()
        fpWrite.close()

    def TransChinese(self,id,strQuestion):
        pos = self.Find(strQuestion,str(id)) 
        if pos>=0:
            pos1 = self.Find(strQuestion,'\n'+str(id),pos) 
            if pos1 > 0:
                return strQuestion[pos1+1:]
            return strQuestion
        else:
            return ''

    def TransTitle(self,id,title):
        if title.rfind('\n') == len(title)-1:
            title = title[0:len(title)-2]

        pos = self.Find(title,str(id))
        if pos >= 0:
            title = '\n' + str(id) + '\t\"'+ title[len(str(id))+1:]+'\"'
        else:
            print(str(id) + " title error!")
        return title


    def TranQuestion(self,id,strQuestion):
        if strQuestion.strip()=='':
            return ''
        strQuestion = self.TransChinese(id,strQuestion)
        if strQuestion == '':
            print(str(id) + " title error.")
            return ''

        head = 0
        strRes = ""
        trail = 0
        strRes = self.TransTitle(id,strQuestion[0:])
        strSign = '参考答案：'
        strAnswer = ''
        pos = strRes.find(strSign)
        if pos >=0 :
            strAnswer = strRes[pos+len(strSign):pos+len(strSign)+1]
        return strRes + '\t' + strAnswer


def main():
    pmp = PMP1(sys.argv[1],sys.argv[2])
    pmp.Trans()

if __name__ == '__main__':
    main()