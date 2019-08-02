#通过位置变量实现字符串的外部输入
import sys
astr = sys.argv[1]

#range('字符串长度') ----> 给每个字符标序号，从而能定位到分片的节点
#for循环+ if判断 ---->   astr[i] 逐个字符遍历，判断出非空值的节点i

for i in range(len(astr)):
    if astr[i] != ' ':
        break
print(astr[i:])
