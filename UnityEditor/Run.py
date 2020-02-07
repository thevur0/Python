import sys
from UnityProjectSvn import UnityProjectSvn

if __name__ == "__main__":
    local_path = sys.argv[1]
    svn_url = sys.argv[2]
    is_update = sys.argv[3]
    is_enable_sdk = sys.argv[4]
    is_clean_ab = sys.argv[5]
    is_enbale_uwa = sys.argv[6]
    update_files = sys.argv[7]
    if len(sys.argv)>8:
        version = sys.argv[8]

    unity_svn = UnityProjectSvn(local_path,svn_url,is_update,update_files,version)
    delete_file = DeleteFile(local_path)

    pass