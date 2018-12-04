import sys,io,os

class PMP2:
    def __init__(self,file1,file2):
        self.file1 = file1
        self.file2 = file2

    def Trans(self):
        
        fp1 = open(self.file1, 'r',encoding='UTF-8')
        fp2 = open(self.file2, 'w',encoding='UTF-8')
        #strSave = ''
        str1 = fp1.read()
        head = 0
        for i in range(1,200):
            trail = str1.find(str(i+1)+".",head)
            if trail < 0:
                trail = str1.find(str(i+1)+" ",head)

            str2 = self.TranQuestion(i,str1[head:trail])
            fp2.writelines(str2)
            head = trail

        str2 = self.TranQuestion(200,str1[trail:])
        fp2.writelines(str2)
        fp1.close()
        fp2.close()

    def TransChinese(self,id,strQuestion):
        pos = strQuestion.find(str(id)+'.')
        if pos < 0:
            pos = strQuestion.find(str(id)+' ')
        if pos>=0:
            pos1 = strQuestion.find('\n'+str(id)+'.',pos)
            if pos1 < 0:
                pos1 = strQuestion.find('\n'+str(id)+' ',pos)
            if pos1 > 0:
                return strQuestion[pos1+1:]
            return strQuestion
        else:
            return ''

    def TransTitle(self,id,title):
        if title.rfind('\n') == len(title)-1:
            title = title[0:len(title)-2]

        pos = title.find(str(id)+'.')
        if pos < 0:
            pos = title.find(str(id)+' ')
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
        for j in range(0,4):
            index = 2
            ch = chr(j+ord('A'))
            head = strQuestion.find(ch +".",trail)

            if head < 0:
                head = strQuestion.find(ch,trail)
                index = 1

            if strRes =='':
                strRes = self.TransTitle(id,strQuestion[0:head])
            trail = strQuestion.find("\n",head)
            strSelection = strQuestion[head:trail]
            strRes = strRes + "\t" + ch + "\t" + strSelection[index:]

        return strRes


def main():
    pmp = PMP2(sys.argv[1],sys.argv[2])
    pmp.Trans()

if __name__ == '__main__':
    main()