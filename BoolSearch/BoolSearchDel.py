import nltk
import collections
from Serching import operateDocList as listSort
from Serching import searchWord as search

# input is a list of query
# 布尔检索的形式如下  a and b or not c
# 这里规定布尔检索的 not 后不能接bool表达式，只能接查询短语或者查询单词
def valueofBoolOp(op):
    precedence = ['OR', 'AND', 'NOT']
    for i in range(3):
        if op == precedence[i]:
            return i
    return -1
#得到后序表达式的栈
def InfxiToPofix(inputList):
    #符号优先级
    precedence = ['OR','AND','NOT']
    precedence ={}
    precedence['OR'] = 0
    precedence['AND'] = 1
    precedence['NOT'] = 2
    pofix_res = []
    tmp = []
    queries = []
    for word in inputList:
        if(word == '('):
            tmp.append('(')
        elif word == ')':
            if len(queries) > 0:
                pofix_res.append(queries)
                queries = []
            sym = tmp.pop()
            while sym != '(':
                pofix_res.append(sym)
                if len(tmp) == 0:
                    print("Incorrect query")
                    exit(1)  #查询错误退出
                    break
                sym = tmp.pop()
        elif word == 'NOT' or word == "OR" or word == 'AND':
            if len(queries) > 0:
                pofix_res.append(queries)
                queries = []
            if(len(tmp) <= 0):
                tmp.append(word)
            else:
                sym = tmp[len(tmp)-1]
                #弹出到左括号为止
                while len(tmp) >0 and sym != '('and precedence[sym] >= precedence[word]:
                    # pop out
                    pofix_res.append(tmp.pop())
                    if(len(tmp) == 0):
                        break
                    sym = tmp[len(tmp) - 1]
                # push in
                tmp.append(word)
        else:
            # put it into a
            queries.append(word)
            #pofix_res.append(word)
    if len(queries) > 0:
        pofix_res.append(queries)
    while len(tmp) > 0:
        pofix_res.append(tmp.pop())
    return pofix_res
#
#input = ["NOT", "(" ,"A" ,"AND","B",")"]
#res = InfxiToPofix(input)
#print(res)
#while len(res) > 0:
#    print(res.pop())

#the bool query function
#def serachtest(Index,wordlist,flag):
#    return ['1','3','10']

def BoolSearch(query, index):
    pofix = InfxiToPofix(query)
    result = []
    #print(pofix)
    queryArray = []
    notTrue = ['1']
    notFalse = ['0']
    nullReturn = []
    limit = len(pofix)
    i = 0
    while i < limit:
        item = pofix[i]
        if item != 'AND'and item !='OR':
            #print(result)
            #lookforword to see if is item
            if i < limit - 1:
                if pofix[i+1] == "NOT":
                    i = i + 1
                    result.append(search.serarchPhraseForBool(index, item, flag=False))
                    #result.append(serachtest(index, item, flag=True))
                else:
                    result.append(search.serarchPhraseForBool(index, item, flag=True))
                    #result.append(serachtest(index, item, flag=False))
            else:
                result.append(search.serarchPhraseForBool(index, item, flag=False))
        elif item == 'AND':
            if len(result) < 2:
                print("illegal query")
                return nullReturn
            else:
                list1 = result.pop()
                list2 = result.pop()
                result.append(listSort.andTwoList(list1,list2))
        elif item == 'OR':
            if len(result) < 2:
                print("illegal query")
                return nullReturn
            else:
                list1 = result.pop()
                list2 = result.pop()
                result.append(listSort.mergeTwoList(list1,list2))
        i += 1
    if len(result) != 1:
        print("illegal query")
        return nullReturn
    else:
        return result.pop()