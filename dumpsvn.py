import time,sys,os

class SvnDump:
	def __init__(self,svnrepositories,name,oldversion):
		self.svnrepositories = svnrepositories
		self.oldversion = oldversion
		self.name = name
		command = "svnlook youngest {}/{}".format(svnrepositories,name)
		result = os.popen(command)
		res = result.read()
		self.curversion = res.splitlines()[0]

	def Dump(self):
		if self.oldversion == self.curversion:
			return self.oldversion
		command = 'svnadmin dump {}/{} --incremental -r {}:{}> {}\{}_{}_{}.dump'.format(self.svnrepositories,self.name,self.oldversion,self.curversion,self.svnrepositories,self.name,self.oldversion,self.curversion)
		os.system(command)
		return self.curversion

def DoDump():
	svnrepositories = sys.argv[1]
	name = sys.argv[2]
	savefilepath = '{}/{}/lastversion.txt'.format(svnrepositories,name)
	verfile = open(savefilepath, 'rw')
	version = verfile.read()
	svn = SvnDump(svnrepositories,name,version)
	version = svn.Dump()


class SvnLoad:
	def __init__(self,svnrepositories,name,file):
		self.svnrepositories = svnrepositories
		self.name = name
		self.file = file

	def Load(self):
		self



def main():
	DoDump()
	##while(True):
		
		##time.sleep(60)
		##pass

if __name__ == '__main__':
	main()