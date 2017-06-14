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
    if len(words) == 0:
        return []
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

def searchPhrase(index,words,inputList):
    if len(words) == 0:
        return []
    docQueue = queue.Queue()
    for word in words:
        docQueue.put(searchOneWord(index,word))

    while docQueue.qsize() > 1:
        list1 = docQueue.get()
        list2 = docQueue.get()
        docQueue.put(operateDocList.andTwoList(list1, list2))
    doclist = docQueue.get()

    resultList = {}

    if len(inputList) == 1:
        for doc in doclist:
            resultList[doc] = index[inputList[0]][str(doc)]
        return resultList

    # print(doclist)
    for docid in doclist:
        docid = str(docid)
        locList = []
        x = index[inputList[0]][docid]
        for loc in index[inputList[0]][docid]:
            # print(index[inputList[0]][docid])
            floc = loc
            n = len(inputList)
            hasFind = True
            for word in inputList[1:n]:
                floc += 1
                try:
                    # print(index[word][docid])
                    index[word][docid].index(floc)
                except:
                    hasFind = False
                    break
            if hasFind:
                locList.append(loc)
        if len(locList) > 0:
            resultList[docid] = locList
    return resultList

