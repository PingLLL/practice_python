#用位置变量调用源文件,目标文件
import sys
src = sys.argv[1]
dest = sys.argv[2]

#为拷贝代码所需的动作定义变量
opensrc = open(src, 'rb')
getsrc = opensrc.readlines()
getdest = open(dest, 'wb')

#真正实现拷贝功能的代码
getdest.writelines(getsrc)

#关闭文件
opensrc.close()
getdest.close()
