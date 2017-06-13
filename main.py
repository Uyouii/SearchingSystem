from InvertedIndex import establishVSM
from InvertedIndex import getIndex
from InvertedIndex import establishIndex

establishIndex.createIndex('test')

index = getIndex.getIndex()
wordList = getIndex.getWordList()

establishVSM.createVSM(index,wordList,'test')
