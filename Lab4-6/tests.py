from ui import *
def test_initContestant():
    assert initContestant() == {'score': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'id': 0}

def test_setScore():
    contestant = initContestant()
    contestant = setScore(contestant, [4, 4, 4, 4, 4, 4, 4, 4, 4, 4])
    assert contestant == {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 0}

def test_getScore():
    contestant = initContestant()
    contestant = setScore(contestant, [1, 10, 2, 5, 3, 6, 7, 8, 9, 10])
    assert getScore(contestant) == [1, 10, 2, 5, 3, 6, 7, 8, 9, 10]

def test_setID():
    contestant = initContestant()
    contestant = setScore(contestant, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    contestant = setID(contestant, 2)
    assert contestant == {'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 2}

def test_getID():
    contestant = initContestant()
    contestant = setID(contestant, 1)
    assert getID(contestant) == 1

def test_score():
    contestant = initContestant()
    contestant = setScore(contestant, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert score(contestant) == 55

def test_newContestant():
    contestants = [
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 2},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 3},
    ]
    contestants = newContestant(contestants, [1, 10, 2, 5, 3, 6, 7, 8, 9, 10])
    assert getID(contestants[3]) == 4 and getScore(contestants[3]) == [1, 10, 2, 5, 3, 6, 7, 8, 9, 10]

def test_delContestant():
    contestants = []
    newContestant(contestants, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert delContestant(contestants, 1) == []

def test_lessThan():
    assert lessThan([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 2},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 3},
    ], 25) == [
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 3},
    ]
def test_moreThan():
    assert moreThan([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 2},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 3},
    ], 25) == [{'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 2}]
def test_sortContestants():
    assert sortContestants([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 2},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 3},
    ]) == [
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 2},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 3},
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1}
    ]

def test_delInterval():
    assert delInterval([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 2},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ], 2,4) == [
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ]

def test_replaceScore():
    assert replaceScore([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 2},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ], 2, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 'id': 2},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ]

def test_updateStack():
    copyStack = [[{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 1}]]
    contestants = [{'score':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 2}]
    copyStack = updateStack(copyStack, contestants)
    assert copyStack == [
        [{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 1}], [{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 2}]
    ]
    copyStack = updateStack(copyStack, contestants)
    assert copyStack == [
        [{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 1}],
        [{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 2}],
        [{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 2}]
    ]

def test_undo():
    contestants = []
    copyStack = [
        [{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 1}], [{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 2}]
    ]
    assert undo(copyStack) == [{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 2}]
    assert copyStack == [
        [{'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'id': 1}]
    ]

def test_averageScore():
    assert averageScore([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 2},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ], 2, 4) == 30

def test_minScore():
    assert minScore([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 2},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ], 2, 4) == 20

def test_multipleOfX():
    assert multipleOfX([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 2},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ], 6) == [{'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3}]

def test_filterMultipleOfX():
    assert filterMultipleOfX([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 2},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ], 6) == [
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 2},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ]

def test_filterLessThan():
    assert filterLessThan([
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 2},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ], 25) == [
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ]

def testAll():
    test_initContestant()
    test_setScore()
    test_getScore()
    test_setID()
    test_getID()
    test_newContestant()
    test_delContestant()
    test_score()
    test_lessThan()
    test_moreThan()
    test_sortContestants()
    test_delInterval()
    test_replaceScore()
    test_updateStack()
    test_undo()
    test_averageScore()
    test_minScore()
    test_multipleOfX()
    test_filterMultipleOfX()
    test_filterLessThan()