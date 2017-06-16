import json
import os

projectpath = 'D:/pythonProject/SearchingSystem/SearchSystem/'
reuterspath = 'D:/pythonProject/SearchingSystem/Reuters'

def writeToFile(item,filename):
    # 将数据写入到文件中
    file = open(filename,'w')
    str = json.JSONEncoder().encode(item)
    file.write(str)
    file.close()

#获取文档名中的文档的id
def getDocID(filename):
    end = filename.find('.')
    docId = filename[0:end]
    return int(docId)

def getWholeDocList():
    files = os.listdir(reuterspath)
    fileList = []
    for file in files:
        fileList.append(getDocID(file))
    return sorted(fileList)

print("getting file list...")
wholeDocList = getWholeDocList()