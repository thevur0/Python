import sys,os,math
sys.path.append("D:\\Program Files\\Autodesk\\3ds Max 2016")
import MaxPlus


def DealWithNodes():
    root = MaxPlus.Core.GetRootNode()

    nodelist = []  
    dellist = []
    for node in root.Children:
        if '(Dummy)' in str(node.Object):
            dellist.append(node)
        elif not 'UCX_' in node.Name:
            parent = node
        else:
            nodelist.append(node)
    
    for child in nodelist:
        parent.AttachChild(child)

    for delchild in dellist:
        delchild.Delete()

def RotatePivot():
    root = MaxPlus.Core.GetRootNode()
    allnodes = Descendants(root)
    for node in allnodes:
        node.SetPivotMode(1)
        node.Rotate(MaxPlus.Quat(-1, 0, 0, 1),0,MaxPlus.Matrix3(1),False,False,1)

def Descendants(node):
    for c in node.Children:
        yield c
        for d in Descendants(c):
            yield d

def main():
    opendir = "D:\\Scr"
    savedir = "D:\\Des"
    if not os.path.isdir(opendir) or not os.path.isdir(savedir):
        return
    
    filelist = os.listdir(opendir)
    for onefile in filelist:
        ext = os.path.splitext(onefile)[1].lower()
        if ext == ".max":
            print(onefile)
            openfile = os.path.join(opendir,onefile)
            savefile = os.path.join(savedir,onefile)
            exportfile = os.path.join(savedir,onefile).replace('.max','.fbx')
            MaxPlus.FileManager.Open(openfile,True,False,False)
            RotatePivot()
            DealWithNodes()
            MaxPlus.FileManager.Export(exportfile,True)
            MaxPlus.FileManager.Save(savefile)
        if ext == ".fbx":
            print(onefile)
            openfile = os.path.join(opendir,onefile)
            savefile = os.path.join(savedir,onefile)
            exportfile = os.path.join(savedir,onefile).replace('.max','.fbx')
            MaxPlus.FileManager.Import(openfile)
            RotatePivot()
            DealWithNodes()
            MaxPlus.FileManager.Export(exportfile,True)
            MaxPlus.FileManager.Reset(True)

if __name__ == '__main__':
	main()





