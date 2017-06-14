from InvertedIndex import establishVSM
from InvertedIndex import getIndex
from InvertedIndex import establishIndex
from LanguageAnalysis import stemming
from Serching import searchWord
from scoreQuery import sortDoc

import tools
import os

directname = 'Reuters'

#establishIndex.createIndex(directname)

print("getting word list...")
wordList = getIndex.getWordList()
print("getting index...")
index = getIndex.getIndex()
print("loading the wordnet...")
stemming.lemmatize_sentence("a")

path = tools.projectpath + directname
files = os.listdir(path)
fileNum = len(files)

print("=================Searching System=================")
print("Input the query statement:")
statement = input()

while statement is not "EXIT":
    #对输入的字符进行词干还原
    inputWords = stemming.lemmatize_sentence(statement)
    print(inputWords)
    #去除input中重复的元素
    wordset = set(inputWords)
    docList = searchWord.searchWords(index,wordset)
    # print(docList)
    sortDoc.sortScoreDocList(index,fileNum,wordset,docList)


    statement = input()



# establishVSM.createVSM(index,wordList,'test')
