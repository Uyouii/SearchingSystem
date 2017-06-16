import os
import tools
from InvertedIndex import getIndex
from LanguageAnalysis import stemming
from Serching import searchWord
from SpellingCorrect import spell
from scoreQuery import sortDoc
from BoolSearch import BoolSearchDel

DIRECTNAME = 'Reuters'

# print("establishing the INDEX...")
# establishIndex.createIndex(DIRECTNAME)

print("getting word list...")
WORDLIST = getIndex.getWordList()
print("getting index...")
INDEX = getIndex.getIndex()
print("loading the wordnet...")
stemming.lemmatize_sentence("a", False)

PATH = tools.projectpath + DIRECTNAME
FILES = os.listdir(tools.reuterspath)
FILENUM = len(FILES)

LOOP = True
print("=================Searching System=================")

while LOOP:
    print("searching operation: ")
    print("[1] Overall [2]TOP K [3]BOOL [4]Phrase [5]wildcard [6]exit")
    print("your choice(int):")
    try:
        choice = int(input())
        if choice == 6:
            break
    except :
        print()
        continue

    if choice >= 1 and choice <= 5:
        print("input the query statement:")
        STATEMENT = input()
        if STATEMENT == "EXIT":
            break

        #查询排序
        if choice == 1:
            print("stemming...")
            INPUTWORDS = stemming.lemmatize_sentence(STATEMENT, True)
            print(INPUTWORDS)
            print("spelling correcting...")
            INPUTWORDS = spell.correctSentence(INPUTWORDS)
            print(INPUTWORDS)

            WORDSET = set(INPUTWORDS)

            DOCLIST = searchWord.searchWords(INDEX, WORDSET)
            SORTEDDOCLIST = sortDoc.sortScoreDocList(INDEX, FILENUM, WORDSET, DOCLIST)
            for doc in SORTEDDOCLIST:
                print("doc ID: ", doc[1], " score: ", "%.4f" % doc[0])

        #TOP K 查询
        elif choice == 2:
            print("stemming...")
            INPUTWORDS = stemming.lemmatize_sentence(STATEMENT, True)
            print(INPUTWORDS)
            print("spelling correcting...")
            INPUTWORDS = spell.correctSentence(INPUTWORDS)
            print(INPUTWORDS)

            WORDSET = set(INPUTWORDS)

            DOCLIST = searchWord.searchWords(INDEX, WORDSET)
            SORTEDDOCLIST = sortDoc.TopKScore(20, INDEX, FILENUM, WORDSET, DOCLIST)
            for doc in SORTEDDOCLIST:
                print("doc ID: ", doc[1], " score: ", "%.3f" % doc[0])
        #Bool 查询
        elif choice == 3:
            print("stemming...")
            INPUTWORDS = stemming.lemmatize_sentence(STATEMENT, True)
            print(INPUTWORDS)
            print("spelling correcting...")
            INPUTWORDS = spell.correctSentence(INPUTWORDS)
            print(INPUTWORDS)

            DOCLIST = BoolSearchDel.BoolSearch(INPUTWORDS, INDEX)
            print("DocList: ")
            print(DOCLIST)
        #短语查询
        elif choice == 4:
            print("stemming...")
            INPUTWORDS = stemming.lemmatize_sentence(STATEMENT, True)
            print(INPUTWORDS)
            print("spelling correcting...")
            INPUTWORDS = spell.correctSentence(INPUTWORDS)
            print(INPUTWORDS)

            WORDSET = set(INPUTWORDS)

            PHRASEDOCLIST = searchWord.searchPhrase(INDEX, WORDSET, INPUTWORDS)
            if 0 == len(PHRASEDOCLIST):
                print("Doesn't find \"", INPUTWORDS, '"')
            else:
                for key in PHRASEDOCLIST:
                    print('docID: ', key, "   num: ", len(PHRASEDOCLIST[key]))
                    print('    location: ', PHRASEDOCLIST[key])
        #模糊查询
        elif choice == 5:
            list = searchWord.wildcardSearch(STATEMENT, INDEX, WORDLIST)
            # for key in list:
            #     # if len(list[key]) == 0:
            #     #     print("    ","doesn't find",key,"in articles")
            #     # else:
            #     if len(list[key]) != 0:
            #         print(key, ":")
            #         print("    DocList: ",list[key])

    else:
        print("Invalid choice! Please observe these choices carefully!")
    print()

print("ByeBye!")


# establishVSM.createVSM(INDEX,WORDLIST,'test')
