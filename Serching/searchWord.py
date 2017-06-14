import queue
from Serching import operateDocList

def searchOneWord(index,word):
    if word not in index:
        return []
    else:
        #将所有文档id变为数字
        docList = [int(key) for key in index[word].keys() ]
        #将文档的id排序
        docList.sort()
        return docList

#将所有word的结果取并，即所有包含这些word的文档
def searchWords(index,words):
    docQueue = queue.Queue()
    #print(wordset)
    for word in words:
        docQueue.put(searchOneWord(index,word))

    while docQueue.qsize() > 1:
        list1 = docQueue.get()
        list2 = docQueue.get()
        docQueue.put(operateDocList.mergeTwoList(list1,list2))

    list = docQueue.get()
    return list
