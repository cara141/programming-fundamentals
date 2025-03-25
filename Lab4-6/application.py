from infrastructure import *
def newContestant(contestants, score):
    contestant = initContestant()

    if len(contestants) == 0:
        contestant = setID(contestant, 1)
    else:
        contestant = setID(contestant, getID(contestants[len(contestants)-1]) + 1)
    contestant = setScore(contestant, score)
    contestants.append(contestant)
    return contestants

def delContestant(contestants, ID):
    index = 0
    for contestant in contestants:
        if getID(contestant) == ID:
            del contestants[index]
        index = index + 1
    return contestants



def lessThan(contestants, upperBound):
    auxList = []
    for count in range(0, len(contestants)):
        if score(contestants[count]) < upperBound:
            auxList.append(contestants[count])
    return auxList





def moreThan(contestants, lowerBound):
    auxList = []
    for count in range(0, len(contestants)):
        if score(contestants[count]) > lowerBound:
            auxList.append(contestants[count])
    return auxList





def sortContestants(contestants):
    auxList = []
    for contestant in contestants:
        auxList.append(contestant)
    if len(auxList) < 2:
        return contestants
    for i in range(0, len(auxList) - 1):
        for j in range(i, len(auxList)):
            if score(auxList[i]) < score(auxList[j]):
                temp = auxList[i]
                auxList[i] = auxList[j]
                auxList[j] = temp
    return auxList


def delInterval(contestants, start, end):
    numDeleted = 0
    for count in range(0, len(contestants)):
        count = count - numDeleted
        if count < len(contestants):
            contestant = contestants[count]
            if start <= getID(contestant) <= end:
                delContestant(contestants, getID(contestant))
                numDeleted = numDeleted + 1

    return contestants

def replaceScore(contestants, ID, newScore):
    auxList = []
    for contestant in contestants:
        auxList.append(contestant)
    count = 0
    for contestant in auxList:
        if getID(contestant) == ID:
            auxList[count] = setScore(auxList[count], newScore)
        count = count + 1
    return auxList
def updateStack(copyStack, contestants):
    if len(copyStack) == 10:
        del copyStack[0]
    auxList = []
    for count in range(0,len(contestants)):
        contestant = contestants[count].copy()
        auxList.append(contestant)
    copyStack.append(auxList)
    return copyStack



def undo(copyStack):
    contestants = copyStack.pop()
    auxList = []
    for contestant in contestants:
        auxList.append(contestant.copy())
    return auxList



def averageScore(contestants, start, end):
    count = 0
    sum = 0
    for contestant in contestants:
        if start <= getID(contestant) <= end:
            sum = sum + score(contestant)
            count = count + 1
    return sum/count



def minScore(contestants, start, end):
    _minScore = 100
    for contestant in contestants:
        if start <= getID(contestant) <= end and score(contestant) <= _minScore:
            _minScore = score(contestant)
    return _minScore


def multipleOfX(contestants, x):
    auxList = []
    for contestant in contestants:
        if score(contestant) % x == 0:
            auxList.append(contestant)
    return auxList



def filterMultipleOfX(contestants, x):
    for contestant in contestants:
        if score(contestant) % x == 0:
            delContestant(contestants, getID(contestant))
    return contestants



def filterLessThan(contestants, minScore):
    auxList = []
    for contestant in contestants:
        if score(contestant) >= minScore:
            auxList.append(contestant)
    return auxList


