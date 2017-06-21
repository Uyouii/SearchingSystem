import os
import tools
from LanguageAnalysis import stemming

def preProcess(filename):
    file = open(filename,'r')
    content = file.read()
    words = stemming.lemmatize_sentence(content,False)
    return words

def processDirectory(directname):
    path = tools.projectpath
    path += directname
    files = os.listdir(path)
    result = []
    for file in files:
        content = preProcess(path + '/' + file)
        result.append(content)
        # print(content)
    return result

#processDirectory('test')