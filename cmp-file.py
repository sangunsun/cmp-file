'''
对两个文件进行比较,输出A-B的结果
输入的两个文件均为文本文件，每条字符串占一行。

使用场景举例：
A是主表的主键，B是子表外键，想知道哪些键值是A表有而B表没有的
或者反过来，想知道哪些键值是B有而A没有的。
'''

aFileName=input("请输入文件名A")
bFileName=input("请输入标准文件名B")

diffList=[]
with open(aFileName) as aFile,open(bFileName) as bFile:
        aLines= aFile.readlines()
        bLines=bFile.readlines()
        
        #去除首尾空格 
        for aIndex in range(len(aLines)):
            aLines[aIndex]=aLines[aIndex].strip()
        for bIndex in range(len(bLines)):
            bLines[bIndex]=bLines[bIndex].strip()
        #---------------------------------
        for aLine in (aLines):
            if aLine  in bLines:
                if aLine not in diffList:
                    diffList.append(aLine)

print(aFileName,"-",bFileName,"文本如下：") 
print()
for row in diffList:
    print(row)
