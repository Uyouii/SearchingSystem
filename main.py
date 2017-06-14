from InvertedIndex import getIndex
from InvertedIndex import establishIndex
from LanguageAnalysis import stemming
from Serching import searchWord
from scoreQuery import sortDoc
import tools
import os

directname = 'Reuters'

# print("establishing the index...")
# establishIndex.createIndex(directname)

print("getting word list...")
wordList = getIndex.getWordList()
print("getting index...")
index = getIndex.getIndex()
print("loading the wordnet...")
stemming.lemmatize_sentence("a")

path = tools.projectpath + directname
files = os.listdir(path)
fileNum = len(files)

loop = True
print("=================Searching System=================")

while loop:
    print("searching operation: ")
    print("[1] Overall Search  [2]TOP K Search [3]bool search [4]Phrase Search [5]exit")
    print("your choice(int):")
    choice = int(input())

    if choice >= 1 and choice <= 5:
        print("input the query statement:")
        statement = input()
        if statement == "EXIT":
            break
        # 对输入的字符进行词干还原
        inputWords = stemming.lemmatize_sentence(statement)
        print(inputWords)
        # 去除input中重复的元素
        wordset = set(inputWords)

        #查询排序
        if choice == 1 :
            docList = searchWord.searchWords(index, wordset)
            sortedDocList = sortDoc.sortScoreDocList(index,fileNum,wordset,docList)
            for doc in sortedDocList:
                print("doc ID: ", doc[1], " score: ", "%.4f" % doc[0])

        #TOP K 查询
        elif choice == 2:
            docList = searchWord.searchWords(index, wordset)
            sortedDocList = sortDoc.TopKScore(20, index, fileNum, wordset, docList)
            for doc in sortedDocList:
                print("doc ID: ", doc[1], " score: ", "%.3f" % doc[0])

        elif choice == 3:
            pass

        elif choice == 4:
            phraseDocList = searchWord.searchPhrase(index,wordset,inputWords)
            if len(phraseDocList) == 0:
                print("Doesn't find \"",statement, '"')
            else:
                for key in phraseDocList.keys():
                    print('docID: ',key, "   num: ",len(phraseDocList[key]))
                    print('    location: ',phraseDocList[key])
        elif choice == 5:
            break
    else:
        print("Invalid choice! Please observe these choices carefully!")
    print()

print("ByeBye!")


# establishVSM.createVSM(index,wordList,'test')
