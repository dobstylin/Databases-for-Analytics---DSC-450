#Daniel OBrien
#DSC 450
#HW 1a

def average(lst):
    newLst = lst.split(',')
    length = len(newLst)
    intLst = []
    for item in newLst:
        intLst.append(int(item))
    res = sum(intLst)/length
    return res

print(average('11, 25, 52, 71, 19'))

#Daniel OBrien
#DSC 450
#HW 1b


def SQLInsert(TName, Lst):
    newLst = (', '.join(Lst))
    return 'INSERT INTO {} VALUES ({})'.format(TName, newLst)

print(SQLInsert('Students', ['15', 'Daniel', 'B+']))