import time,sys,os

class SvnOperation:
    def __init__(self):

        checkCommand = 'svn checkout %s %s' %(svnPath,localPath)
        switchCommand = 'svn switch %s --force --accept theirs-full'% svnPath
        cleanupCommand = 'svn cleanup'
        revertCommand = 'svn revert %s ==depth=infinity'
        statusCommand = 'svn status %s --ignort-externals --depth infinity'
        deleteCommand = 'svn delete --force %s'%filePath
        updateCommand = 'svn update %s theirs-full'
        updateVersionCommand = 'svn update %s -r %s their-full'
		os.system(command)
        pass
    pass
 
if __name__ == "__main__":
    pass