def SCP(ip, user_name, passwd):
    import os
    import sys
    user_name = sys.argv[2]
    passwd = sys.argv[3]
    ip = sys.argv[1]
    os.system('scp ')