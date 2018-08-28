import os,sys,string,datetime,time
class DealwithFIle(object):
	"""docstring for DealwithFIle"""
	def __init__(self, arg1,arg2):
		super(DealwithFIle, self).__init__()
		self.path = arg1
		self.savepath = arg2
		
	def modify(self):
		with open(self.path,"rb") as fp:
			byData = fp.read()
			strSave = ''
			ilen = len(byData)
			limitlen = 1024*1024*4
			if ilen>limitlen:
				ilen = limitlen

			for x in range(0,ilen):
				strSave += chr(255 - (byData[x]))
				#print(ilen,":",x,byData[x])
			pass
			byDateSave = strSave.encode('latin1')
			byDateSave = byDateSave + byData[ilen:]

		with open(self.savepath,"wb") as fp:
			fp.write(byDateSave)
		print(self.path,">>>>>>>>>>>>>>>",self.savepath)

 
def main():
	
	if os.path.isfile(sys.argv[1]) and not os.path.isdir(sys.argv[2]):
		dwFile = DealwithFIle(sys.argv[1],sys.argv[2])
		dwFile.modify()
		pass
	elif os.path.isfile(sys.argv[1]) and os.path.isdir(sys.argv[2]):
		savePath = os.path.join(sys.argv[2],os.path.basename(sys.argv[1]))
		dwFile = DealwithFIle(sys.argv[1],savePath)
		dwFile.modify()
		pass
	elif os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):
		for root, dirs, files in os.walk(sys.argv[1]):
			for onefile in files:  
				savePath = os.path.join(sys.argv[2],os.path.basename(onefile))
				dwFile = DealwithFIle(os.path.join(root ,onefile),savePath)
				dwFile.modify()
		pass
	pass
if __name__ == '__main__':
	main()
