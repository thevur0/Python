import time,sys,os
import subprocess

class SvnOperation:
    def __init__(self,local_path,svn_path):
        self.svn_path = svn_path
        self.local_path = local_path

        (ret, out, err) = self.run_command('svn')
        svn_enable = False

        if str(err, encoding="utf-8").find('svn help') != -1:
            svn_enable = True

        if svn_enable == False:
            raise Exception("sdfsadfasf")

        pass

    def info(self,attribute):
        info_command = 'svn info %s' % self.local_path
        result = os.popen(info_command).read()
        lines = str(result).split('\n')
        for line in lines:
            pair = line.split(':',1)
            if len(pair) == 2:
                if pair[0] == attribute:
                    return pair[1].strip()
                    
        return ''
    def checkout(self):
        checkOut_command = 'svn checkout %s %s' %(self.svnPath,self.local_path)
        self.os_command(checkOut_command)

    def switch(self):
        switch_command = 'svn switch %s %s --force --accept theirs-full --ignore-ancestry'% (self.svnPath,self.localPath)
        self.os_command(switch_command)

    def cleanup(self,path=''):
        if path == '':
            path = self.local_path
        else:
            path = os.path.join(self.local_path,path)
        cleanup_command = 'svn cleanup %s'%path
        self.os_command(cleanup_command)

    def revert(self,path=''):
        if path == '':
            path = self.local_path
        else:
            path = os.path.join(self.local_path,path)
        revert_command = 'svn revert "%s" --depth=infinity'%path
        self.os_command(revert_command)

    def status(self,path):
        status_command = 'svn status %s --ignort-externals --depth infinity' % path
        self.os_command(status_command)
    
    def delete(self,filePath):
        delete_command = 'svn delete --force %s'%filePath
        self.os_command(delete_command)
        
    def update(self,path='',version=''):
        if path == '':
            path = self.local_path
        else:
            path = os.path.join(self.local_path,path)

        update_command = 'svn update %s theirs-full'%path
        if version != '':
            update_command = 'svn update %s -r %s theirs-full' %(path,version)
        self.os_command(update_command)

    def os_command(self,command):
        print(command)
        os.system(command)

    def run_command(self,cmd):
        # Popen call wrapper.return (code, stdout, stderr)
        child = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        out, err = child.communicate()
        ret = child.wait()
        return (ret, out, err)

class UnityProjectSvn:
    revert_paths = ['Assets','ProjectSettings','Wwise Project','Wwise MouthProject','TempRes']
    def __init__(self,local_path,svn_path,is_update,update_files,version=''):
        svn = SvnOperation(local_path,svn_path)
        cur_svn_path = svn.info("URL")
        if  cur_svn_path.lower() != svn_path.lower():
            svn.switch()
        if is_update == False:
            return
        svn.cleanup()

        for revert_path in self.revert_paths:
            svn.revert(revert_path)
        if update_files=='':
            svn.update('',version)
        else:
            file_list = update_files.split(';')
            for update_file in file_list:
                svn.update(update_file)
        pass
    pass
 
if __name__ == "__main__":
    print("UnityProjectSvn Main")
    pass