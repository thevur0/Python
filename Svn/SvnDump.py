import time,sys,os

class SvnDump:
	def __init__(self,svnrepositories,name,oldversion,dumppath):
		self.svnrepositories = svnrepositories
		self.oldversion = oldversion
		self.name = name
		self.dumppath = dumppath
		command = "svnlook youngest {}/{}".format(svnrepositories,name)
		result = os.popen(command)
		res = result.read()
		self.curversion = res.splitlines()[0]

	def Dump(self):
		if self.oldversion == self.curversion:
			return self.oldversion
		starversion = int(self.oldversion) + 1
		starversion = min(starversion,int(self.curversion))
		command = 'svnadmin dump {}/{} --incremental -r {}:{}> {}\{}_{}_{}.dump'.format(self.svnrepositories,self.name,starversion,self.curversion,self.dumppath,self.name,self.oldversion,self.curversion)
		os.system(command)
		return self.curversion

def DoDump():
	svnrepositories = sys.argv[1]
	name = sys.argv[2]
	dumppath = sys.argv[3]
	savefilepath = '{}/{}/lastversion.txt'.format(svnrepositories,name)
	version = 0
	if os.path.exists(savefilepath):
		verfile = open(savefilepath, 'r')
		version = verfile.read()
		verfile.close()

	svn = SvnDump(svnrepositories,name,version,dumppath)
	newversion = svn.Dump()
	verfile = open(savefilepath, 'w')
	if newversion > version:
		version = newversion
		verfile.write(version)
	verfile.close()

def main():
	DoDump()
	while(True):
		DoDump()
		time.sleep(10)
		##pass

if __name__ == '__main__':
	main()