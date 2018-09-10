import time,sys,os

class SvnLoad:
	def __init__(self,svnrepositories,name,dpfile):
		self.svnrepositories = svnrepositories
		self.name = name
		self.file = dpfile

	def Load(self):
		print(self.file)
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
				dumpfile = os.path.join(dpPath ,onefile)
				if ext == ".dump":
					svn = SvnLoad(svnrepositories,name,dumpfile)
					svn.Load()
					os.remove(dumpfile)
					
				

def main():
	DoLoad()
	##while(True):
		##time.sleep(60)
		##pass

if __name__ == '__main__':
	main()