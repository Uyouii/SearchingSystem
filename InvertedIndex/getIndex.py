import json
import tools


def getIndex():
    file = open(tools.projectpath + 'invertIndex.json', 'r')
    indexStr = file.read()
    index = json.JSONDecoder().decode(indexStr)
    return index

def getWordList():
    file = open(tools.projectpath + 'wordList.json', 'r')
    wordStr = file.read()
    wordList = json.JSONDecoder().decode(wordStr)
    return wordList

# print(getWordList())