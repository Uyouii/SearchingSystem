from scoreQuery import getScore

def getScoreDocList(index,fileNum, words,docList):
    scoreDocList = []
    for doc in docList:
        score = getScore.get_wfidf_Score(index,fileNum,doc,words)
        #scoreDocList 是score和doc的tuple
        scoreDocList.append((score,doc))
    #print(scoreDocList)
    return scoreDocList

#从大到小得到sortedDocList
def sortScoreDocList(index,fileNum,words,docList):
    scoreDocList = getScoreDocList(index,fileNum,words,docList)
    sortedDocList = sorted(scoreDocList,reverse = True)
    print(sortedDocList)
    return sortedDocList