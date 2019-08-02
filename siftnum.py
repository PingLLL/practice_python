import sys
astr = sys.argv[1]
#sift = sys.argv[2]
sift = '1234567890'
result = ''

#可排除数值类型或字符类型的判断，直接把需要输出的数字当作字符处理
for i in range(len(astr)):
    if astr[i] in sift:
        result += astr[i]
print(result)
