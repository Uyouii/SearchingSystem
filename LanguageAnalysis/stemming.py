import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag

#下载需要的依赖文件
# nltk.download("wordnet")
# nltk.download("averaged_perceptron_tagger")
# nltk.download("punkt")
# nltk.download("maxnet_treebank_pos_tagger")


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

deleteSignal = [',','.',';','&',':','>',"'",'`','(',')','+','!','*','"','?']

def lemmatize_sentence(sentence):
    res = []
    result = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(word_tokenize(sentence)):
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))

    for word in res:
        #如果是 's什么的，直接排除
        if word[0] is '\'':
            continue

        #去除标点符号
        for c in deleteSignal:
            word = word.replace(c,'')

        #排除空的字符串
        if len(word) is 0 or word[0] is '-':
            continue

        #如果分解的单词中有/,则将其中的每个单词添加到结果中
        if word.find('/') > 0:
            rs = word.split('/')
            for w in rs:
                w = getWord(w)
                result.append(w)
        else:
            word = getWord(word)
            result.append(word)

    return result

def getWord(word):
    if word.istitle():
        word = word.lower()
        word = WordNetLemmatizer().lemmatize(word, pos='n')
    else:
        word = WordNetLemmatizer().lemmatize(word, pos='n')
    return word

# while 1:
#     str = input()
#     result = lemmatize_sentence(str)
#     for word in result:
#         print(word)

#print(WordNetLemmatizer().lemmatize('probable', pos='v'))