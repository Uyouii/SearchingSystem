
def mergeTwoList(list1,list2):
    rlist = []
    len1 = len(list1)
    len2 = len(list2)
    n1 = 0
    n2 = 0
    while n1 < len1 and n2 < len2 :
        if list1[n1] < list2[n2]:
            rlist.append(list1[n1])
            n1 += 1
        elif list1[n1] > list2[n2]:
            rlist.append(list2[n2])
            n2 += 1
        else:
            rlist.append(list1[n1])
            n1 += 1
            n2 += 1

    if n1 < len1:
        rlist.extend(list1[n1 : len1])
    if n2 < len2:
        rlist.extend(list2[n2 : len2])
    return rlist



def andTwoList(list1,list2):
    rlist = []
    len1 = len(list1)
    len2 = len(list2)
    n1 = 0
    n2 = 0
    while n1 < len1 and n2 < len2:
        if list1[n1] < list2[n2]:
            n1 += 1
        elif list1[n1] > list2[n2]:
            n2 += 1
        else:
            rlist.append(list1[n1])
            n1 += 1
            n2 += 1
    return rlist


# list1 = [1,3,4,5,6,7,9,10]
# list2 = [2,4,6,8,10,12]