import copy
def initContestant():
    default_contestant = {'score': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'id': 0}
    return default_contestant


def setScore(contestant, newScore):
    contestant['score'] = newScore
    return contestant

def getScore(contestant):
    return contestant['score']

def setID(contestant, newID):
    contestant['id'] = newID
    return contestant

def getID(contestant):
    return contestant['id']


def score(contestant):
    sum = 0
    for point in getScore(contestant):
        sum = sum + point
    return sum

def validNatural(value):
    try:
        value = int(value)
        if value <= 0:
            return 0
        else:
            return 1
    except ValueError:
        return 0

def validScore(value):
    if len(value) != 10:
        return 0
    for point in value:
        if validNatural(point) == 0:
            return 0
        if int(point) > 10:
            return 0
        return 1

def validID(value, contestants):
    if validNatural(value) == 0:
        return 0
    found = 0
    for contestant in contestants:
        if getID(contestant) == value:
            return 1
    if found != 1:
            return 0

def parseInt(list):
    auxList = list
    for i in range(0, len(list)):
        auxList[i] = int(auxList[i])
    return auxList