import json

projectpath = 'D:/pythonProject/SearchingSystem/'

def writeToFile(item,filename):
    # 将数据写入到文件中
    file = open(filename,'w')
    str = json.JSONEncoder().encode(item)
    file.write(str)
    file.close()
