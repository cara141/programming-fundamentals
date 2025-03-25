from tests import *
def run():
    testAll()
    contestantList = [
        {'score': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'id': 1},
        {'score': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'id': 2},
        {'score': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'id': 3},
        {'score': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'id': 4},
        {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'id': 5}
    ]
    copyStack = []
    maxID = 255
    while True:
        command = input(">>>").split(" ")
        match command[0]:
            case "exit":
                exit()
            case "add":
                updateStack(copyStack, contestantList)
                if (len(contestantList) == maxID):
                    print("Nu se mai pot adauga participanti. Numarul maxim a fost atins.")
                else:
                    if validScore(command[1:]) == 1:
                        score = command[1:]
                        score = parseInt(score)
                        contestantList = newContestant(contestantList, score)
                    else:
                        print("Input invalid")

            case "delete":
                updateStack(copyStack, contestantList)
                if(len(contestantList) == 0):
                    print("Nu exista niciun candidat in lista.")
                else:
                    if validNatural(command[1]) == 0:
                        print("ID invalid")
                    elif validID(int(command[1]), contestantList) == 1:
                        delContestant(contestantList, int(command[1]))
                    else:
                        print("ID invalid")

            case "show":
                match(command[1]):
                    case "less":
                        filteredContestants = lessThan(contestantList, int(command[2]))
                        for contestant in filteredContestants:
                            print("Candidatul nr.", getID(contestant), "a obtinut urmatoarele scoruri:", getScore(contestant),
                                "si are scorul mai mic decat numarul dat")
                    case "sorted":
                        sortedContestants = (sortContestants(contestantList))
                        for contestant in sortedContestants:
                            print("Candidatul nr.", getID(contestant), "a obtinut urmatoarele scoruri:", getScore(contestant))
                    case "more":
                        filteredContestants = moreThan(contestantList, int(command[2]))
                        for contestant in filteredContestants:
                            print("Candidatul nr.", getID(contestant), "a obtinut urmatoarele scoruri:", getScore(contestant),
                                "si are scorul mai mare decat numarul dat")
                    case _:
                        print("Comanda incorecta.")
            case "6":
                updateStack(copyStack, contestantList)
                delInterval(contestantList, inputIntervalBound(), inputIntervalBound())

            case "replace":
                updateStack(copyStack, contestantList)
                if validNatural(command[1]) == 0:
                    print("Invalid input")
                elif validID(int(command[1]), contestantList) and validScore(command[2:]):
                    score = command[2:]
                    parseInt(score)
                    contestantList = replaceScore(contestantList, int(command[1]), score)
                else:
                    print("Invalid input")
            case "undo":
                if len(copyStack) == 0:
                    print("Nu se mai poate da inapoi.")
                else:
                    contestantList = undo(copyStack)
            case "9":
                updateStack(copyStack, contestantList)
                print("Media pe intervalul dat este", averageScore(contestantList, inputIntervalBound(), inputIntervalBound()))
            case "10":
                updateStack(copyStack, contestantList)
                print("Scorul minim al participantilor pe intervalul dat este",
                      minScore(contestantList, inputIntervalBound(), inputIntervalBound()))
            case "11":
                updateStack(copyStack, contestantList)
                filteredContestants = multipleOfX(contestantList, inputNatural())
                for contestant in filteredContestants:
                    print("Candidatul nr.", getID(contestant), "a obtinut urmatoarele scoruri:", getScore(contestant),
                          "si are scorul multiplu de numarul dat.")
            case "12":
                updateStack(copyStack, contestantList)
                contestantList = filterMultipleOfX(contestantList, inputNatural())

            case "13":
                updateStack(copyStack, contestantList)
                contestantList = filterLessThan(contestantList, inputBound())
            case _:
                print("Nu exista aceasta optiune. Va rog alegeti alta.")