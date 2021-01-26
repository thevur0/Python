import io
import os
import sys
import xml.etree.ElementTree as ET
import shutil

def WriteManifest(packageFolder,channelID):
    namespace = '{http://schemas.android.com/apk/res/android}'
 
    #android danger-permission list
    dangerPermissionArray = ['android.permission.READ_CALENDAR',
                            'android.permission.WRITE_CALENDAR',
                            'android.permission.CAMERA',
                            'android.permission.WRITE_CONTACTS',
                            'android.permission.GET_ACCOUNTS',
                            'android.permission.READ_CONTACTS',
                            'android.permission.ACCESS_FINE_LOCATION',
                            'android.permission.ACCESS_COARSE_LOCATION',
                            'android.permission.RECORD_AUDIO',
                            'android.permission.READ_CALL_LOG',
                            'android.permission.READ_PHONE_STATE',
                            'android.permission.CALL_PHONE',
                            'android.permission.WRITE_CALL_LOG',
                            'android.permission.USE_SIP',
                            'android.permission.PROCESS_OUTGOING_CALLS',
                            'com.android.voicemail.permission.ADD_VOICEMAIL',
                            'android.permission.BODY_SENSORS',
                            'android.permission.READ_SMS',
                            'android.permission.RECEIVE_WAP_PUSH',
                            'android.permission.RECEIVE_MMS',
                            'android.permission.RECEIVE_SMS',
                            'android.permission.SEND_SMS',
                            'android.permission.READ_CELL_BROADCASTS',
                            'android.permission.READ_EXTERNAL_STORAGE',
                            'android.permission.WRITE_EXTERNAL_STORAGE']
 
    #uses-permissions list
    usesPermissionArray = []
    
    #danger uses-permission list
    dangerUsesPermissionArray = []
    manifestPath = os.path.join(packageFolder,'AndroidManifest.xml')
    tree = ET.parse(manifestPath)
    root = tree.getroot()
    
    #get packageName and print
    packageName = root.attrib['package']
    print(' ----------------')
    print('|APK packagename:\n ----------------\n'+packageName,'\n')
    
    #get permission and print
    print(' ---------------')
    print('|APK permission:\n ---------------')
    for child in root.iter('uses-permission'):
        childName = child.get(namespace+'name')
        usesPermissionArray.append(childName)
        print(childName)
    
        if (dangerPermissionArray.count(childName)) > 0 :
            dangerUsesPermissionArray.append(childName)
    
    application_node = root.find("application")
    for child in application_node.iter('meta-data'):
        name = child.get(namespace+"name")
        if name == "AppLogId":
            child.set(namespace+"value","XXX")
            pass
        elif name == "AppLogChannel":
            child.set(namespace+"value",channelID)
            pass

    tree.write(manifestPath)
    #print('-------------------------------------------\nall work done with finding ',len(usesPermissionArray),' permissions\n                           ',len(dangerUsesPermissionArray),' are danger!\n-------------------------------------------')
    
def WriteStringXml(packageFolder,channelName):
    stringPath = os.path.join(packageFolder,'res/values/strings.xml')
    tree = ET.parse(stringPath)
    root = tree.getroot()
    for child in root.iter('string'):
        name = child.get("name")
        if name == "app_name":
            child.text = channelName
            pass
    tree.write(stringPath,encoding='utf-8')

if __name__ == "__main__":
    
    apk_name = sys.argv[1]
    resource_folder = sys.argv[2]
    channel_id = sys.argv[3]
    package_folder = apk_name.lower().replace('.apk','')

    if not os.path.exists(apk_name):
        print('{0}不存在'.format(apk_name))
        sys.exit()
    
    if '.apk' not in apk_name.lower():
        print('{0}不是apk'.format(apk_name))
        sys.exit()

    if not channelToName[channel_id]:
        sys.exit()

    #清理目录
    if os.path.exists(package_folder):
        shutil.rmtree(package_folder)
    #解包
    os.system('apktool.bat d {0} -f'.format(apk_name))
    #复制资源
    channel_folder = os.path.join(resource_folder,channel_id)
    for root, dirs, files in os.walk(channel_folder):
        for onefile in files:
            srcfile = os.path.join(root,onefile)
            desfile = srcfile.replace(channel_folder,package_folder)
            print('复制%s=>%s'% (srcfile,desfile))
            shutil.copy(srcfile,desfile)
    #写Manifest.xml
    WriteManifest(package_folder,channel_id)
    #写String.xml
    WriteStringXml(package_folder,channelToName[channel_id])
    #打包
    os.system('call apktool.bat b {0}'.format(package_folder))
    srcfile='{0}/dist/{1}.apk'.format(package_folder,os.path.basename(package_folder))
    desfile='output/nosign_{0}.apk'.format(channel_id)
    if os.path.exists(desfile):
        os.remove(desfile)
    print('复制%s=>%s'% (srcfile,desfile))
    shutil.copy(srcfile,desfile)
    pass