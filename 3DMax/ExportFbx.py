import sys
sys.path.append("D:\\Program Files\\Autodesk\\3ds Max 2016")
import MaxPlus


def DealWithNodes():
    root = MaxPlus.Core.GetRootNode()

    nodelist = []  

    for node in root.Children:
        if not 'UCX_' in node.Name:
            parent = node
        else:
            nodelist.append(node)
    
    for child in nodelist:
        parent.AttachChild(child)

def main():
    openfile = "D:\\Public_Ship_04.max"
    savefile = "E:\\Public_Ship_04.max"
    exportfile = "E:\\Public_Ship_04.fbx"
    MaxPlus.FileManager.Open(openfile,True,False,False)

    DealWithNodes()
    MaxPlus.FileManager.Export(exportfile,True)
    MaxPlus.FileManager.Save(savefile)

if __name__ == '__main__':
	main()





