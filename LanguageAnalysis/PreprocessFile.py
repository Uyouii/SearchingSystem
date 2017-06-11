import os
from LanguageAnalysis import stemming

def preProcess(filename):
    file = open(filename,'r')
    content = file.read()
    words = stemming.lemmatize_sentence(content)
    print(words)

def processDirectory(directname):
    path = 'D:/pythonProject/SearchingSystem/'
    path += directname
    files = os.listdir(path)
    for file in files:
        content = preProcess(path + '/' + file)

processDirectory('Reuters')