import queue
import os
import tools
import re
from Serching import operateDocList


def searchOneWord(index, word):
    if word not in index:
        return []
    else:
        # 将所有文档id变为数字
        docList = [int(key) for key in index[word].keys()]
        # 将文档的id排序
        docList.sort()
        return docList


# 将所有word的结果取并，即所有包含这些word的文档
def searchWords(index, words):
    if len(words) == 0:
        return []
    docQueue = queue.Queue()
    # print(wordset)
    for word in words:
        docQueue.put(searchOneWord(index, word))

    while docQueue.qsize() > 1:
        list1 = docQueue.get()
        list2 = docQueue.get()
        docQueue.put(operateDocList.mergeTwoList(list1, list2))

    list = docQueue.get()
    return list


def searchPhrase(index, words, inputList):
    if len(words) == 0:
        return []
    docQueue = queue.Queue()
    for word in words:
        docQueue.put(searchOneWord(index, word))

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


def serarchPhraseForBool(index, wordList,flag):
    if len(wordList) == 0:
        return []
    docQueue = queue.Queue()
    for word in wordList:
        docQueue.put(searchOneWord(index, word))

    while docQueue.qsize() > 1:
        list1 = docQueue.get()
        list2 = docQueue.get()
        docQueue.put(operateDocList.andTwoList(list1, list2))
    doclist = docQueue.get()

    if len(wordList) == 1:
        if flag:
            return doclist
        else:
            return operateDocList.listNotcontain(tools.wholeDocList,doclist)

    reslist = []

    for docid in doclist:
        docid = str(docid)
        locList = []
        x = index[wordList[0]][docid]
        for loc in index[wordList[0]][docid]:
            # print(index[inputList[0]][docid])
            floc = loc
            n = len(wordList)
            hasFind = True
            for word in wordList[1:n]:
                floc += 1
                try:
                    # print(index[word][docid])
                    index[word][docid].index(floc)
                except:
                    hasFind = False
                    break
            if hasFind:
                reslist.append(int(docid))
                break
    if flag:
        return reslist
    else:
        return operateDocList.listNotcontain(tools.wholeDocList,reslist)



def wildcardSearch(statement,index,wordList):
    words = statement.split(' ')
    #print(words)
    forSearchList = []

    for word in words:
        rset = searchBasedOnWildcard(word,wordList)
        if len(rset) > 0:
            forSearchList.append(rset)
        else:
            print(word,"doesn't find matching words in these articles.")
            return []

    i = 0
    numList = []
    N = len(forSearchList)
    while i < N:
        numList.append(0)
        i += 1

    resultList = {}

    while 1:
        searchList = []
        statement = ""
        j = 0
        while j < N:
            searchList.append(forSearchList[j][numList[j]])
            statement += searchList[j] + " "
            j += 1

        docList = searchPhrase(index,set(searchList),searchList)

        resultList[statement] = docList
        if len(docList) > 0:
            print(statement, ":")
            print("    DocList: ", docList)

        j = 0
        while j < N:
            if numList[j] < len(forSearchList[j]) - 1:
                numList[j] += 1
                m = 0
                while m < j:
                    numList[m] = 0
                    m += 1

                break
            j += 1

        if j >= N:
            break

    return resultList






def wildcard2regex(wildcard):
    regex = '^'
    for i in range(wildcard.__len__()):
        if(i == 0):
            if (wildcard[i] == '*'):
                regex = regex + '[a-z]*'
            elif (wildcard[i] == '?'):
                regex = regex + '[a-z]'
            elif (not wildcard[i].isalpha()):
                return None
            else:
                regex = regex + wildcard[i]
        else:
            if(wildcard[i] == '*'):
                regex = regex + '[a-z]*'
            elif (wildcard[i] == '?'):
                regex = regex + '[a-z]'
            elif (not wildcard[i].isalpha()):
                return None
            else:
                regex = regex + wildcard[i]
    regex = regex + '$'
    return regex

'''
e.g.
ret = searchBasedOnWildcard('f*bility', ['feasability', 'family', 'hello', 'flexibility'])
print(ret)

show: {'feasability', 'flexiblility'}
'''
def searchBasedOnWildcard(wildcard, wordList):
    result = []
    regex = wildcard2regex(wildcard)
    if(regex == None):
        return result
    pattern = re.compile(regex, flags=re.IGNORECASE)
    for word in wordList:
        if(pattern.match(word)):
            result.append(word)
            # print(word)
    return result
        






