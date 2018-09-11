import time,sys,os

class SvnLoad:
	def __init__(self,svnrepositories,name,dpfile):
		self.svnrepositories = svnrepositories
		self.name = name
		self.file = dpfile

	def Load(self):

		command = "svnlook youngest {}/{}".format(self.svnrepositories,self.name)
		result = os.popen(command)
		res = result.read()
		curversion = res.splitlines()[0]
		strFileName = self.name + '_' + curversion + '_'
		findres = os.path.basename(self.file).find(strFileName)
		if findres == 0:
			command = 'svnadmin load {}/{} < {}'.format(self.svnrepositories,self.name,self.file)
			os.system(command)


def DoLoad():
	svnrepositories = sys.argv[1]
	name = sys.argv[2]
	dpPath = sys.argv[3]
	if os.path.isdir(dpPath):
		for root, dirs, files in os.walk(dpPath):
			for onefile in files:
				ext = os.path.splitext(onefile)[1]
				if ext == ".dump":
					dumpfile = os.path.join(dpPath ,onefile)
					svn = SvnLoad(svnrepositories,name,dumpfile)
					svn.Load()
					#os.remove(dumpfile)
def main():
	while(True):
		DoLoad()
		time.sleep(10)

if __name__ == '__main__':
	main()