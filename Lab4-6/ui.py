from application import *
def inputScore():
    print("Introdu 10 numere cuprinse intre 1 si 10")
    count = 0
    score = []
    while count < 10:
        point = input()
        try:
            point = int(point)
            if point in range(1, 11):
                score.append(point)
                count += 1
            else:
                print("Nu este intre 1 si 10")
        except ValueError:
            print("Nu este numar intreg!")

    return score

def inputBound():
    print("Introdu o valoare intre 10 si 100")
    while True:
        bound = input()
        try:
            bound = int(bound)
            if bound in range(10, 101):
                return bound
            else:
                print("Nu este intre 10 si 100")
        except ValueError:
            print("Nu este numar intreg!")


def inputID(contestants):
    print("Introdu un numar de ordine al unui candidat:")
    while True:
        position = input()
        try:
            position = int(position)
            found = 0
            for contestant in contestants:
                if getID(contestant) == position:
                    found = 1
                    return position
            if found != 1:
                print("Nu exista. Introduceti alt numar de ordine.")

        except ValueError:
            print("Nu este numar intreg.")



def inputIntervalBound():
    """
    Cere utilizatorului un numar intreg mai mare decat 1. Valideaza input ul si il returneaza
    preconditii: -
    postconditii: -
    """
    print("Introduceti un numar intreg mai mare decat 1")
    while True:
        bound = input()
        try:
            bound = int(bound)
            if bound > 0:
                return bound
            else:
                print("Nu este mai mare decat 1!")
        except ValueError:
            print("Nu este numar intreg!")

def inputNatural():
    print("Introduceti un numar natural nenul")
    while True:
        try:
            x = int(input())
            if x <= 0:
                print("Nu este natural.")
            else:
                return x
        except ValueError:
            print("Nu este numar intreg.")



