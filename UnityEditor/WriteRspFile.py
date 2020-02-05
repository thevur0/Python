import os
import sys
class WriteRspFile:
    
    noWarningList = []
    defineList =[]
    
    def __init__(self,assetPath,rspName,defineNames):
        self.rspPath = os.path.join(assetPath,rspName)

        if os.path.exists(self.rspPath):
            with open(self.rspPath,"r") as fp:
                lines = fp.readlines()
                for line in lines:
                    pair = line.split(':')
                    if len(pair) == 2:
                        if pair[0] == '-nowarn':
                            self.AddNoWarning(pair[1])
                        elif pair[0] == '-define':
                            self.AddDefine(pair[1])
                    else:
                        Exception ("Prase Error.")

        for defineName in defineNames:
            self.AddDefine(defineName)

        self.SaveFile()

    def AddDefine(self,defineName):
        defineName = defineName.replace('\n','')
        if not defineName in self.defineList:
            self.defineList.append(defineName)
    
    def DeleteDefine(self,defineName):
        defineName = defineName.replace('\n','')
        if defineName in self.defineList:
            self.defineList.remove(defineName)
    
    def AddNoWarning(self,warningName):
        warningName = warningName.replace('\n','')
        if not warningName in self.noWarningList:
            self.noWarningList.append(warningName)

    def SaveFile(self):
        with open(self.rspPath,"w") as fp:
            for noWarning in self.noWarningList:
                fp.write('-nowarn:%s\n'%noWarning)

            for defineName in self.defineList:
                fp.write('-define:%s\n'%defineName)
            
if __name__ == "__main__":
    assetPath = sys.argv[1]
    rspName = sys.argv[2]
    defineNames = sys.argv[3].split('|')
    writeRsp = WriteRspFile(assetPath,rspName,defineNames)
    pass
    