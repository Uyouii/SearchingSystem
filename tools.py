import json

projectpath = 'D:/pythonProject/SearchingSystem/'

def writeToFile(item,filename):
    # 将数据写入到文件中
    # indexfile = open(projectpath + 'invertIndex.json', 'w')
    # invertStr = json.JSONEncoder().encode(invertedIndex)
    # indexfile.write(invertStr)
    # indexfile.close()
    file = open(filename,'w')
    str = json.JSONEncoder().encode(item)
    file.write(str)
    file.close()