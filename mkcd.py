import os
import sys

# 创建新的目录并进入新目录
# mkcd

try :
    print(sys.argv[1])
    dirName = sys.argv[1]
    dirNameExist = os.path.exists(dirName)
    if dirNameExist == False :
        print(dirNameExist)
        os.mkdir(dirName)
        # os.system("cd ls.py1")
        # os.startfile(dirName)
    else:
        print("文件目录存在！！！")
except Exception as e :
    print(e)
finally : 
    print("Done!!!")
