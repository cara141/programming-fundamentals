from Domain.entities import  Tractor
from Repository.repository import TractorRepository
from Controller.controller import TractorController

class UI():
    """
    UI aplicatie
    """
    def __init__(self, nume_fisier):
        """
        Initialziare UI
        :param nume_fisier: numele fisierului de unde trage
        """
        self.Controller = TractorController(nume_fisier)

    def run(self):
        """
        executia programului
        :return: None
        """
        while True:
            print("""
                1.adauga tractor
                2.sterge tractoare
                3.filtreaza tractoare
                4.undo
                """)

            for tractor in self.get_all_filtered():
                print(tractor.__str__())
            line = input(">>>")
            match line:
                case "1":
                    print("introduceti date despre tractor:")
                    tractor_id = int(input("id:"))
                    name = input("denumire:")
                    price = int(input("pret:"))
                    model = input("model:")
                    data = input("data:")
                    try:
                        tractor = Tractor(tractor_id, name, price,  model, data)
                        self.adauga_tractor(tractor)
                    except ValueError:
                        print("Deja exista!")
                case "2":
                    line = input("introduceti o cifra:")
                    line.split(" ")
                    try:
                        price1 = int(line)
                        if 0 <= price1 <= 9:
                            try:
                                count = self.sterge_tractoare(price1)
                                print(f"Numarul de tractoare sterse: {count}")
                            except ValueError:
                                print("Nu se mai poate sterge!")
                    except ValueError:
                        print("Nu este numar intreg!")

                case "3":
                    filtru_nume = input("introduceti filtru pentru denumire:")
                    filtru_pret = input("introduceti filtru pentru pret:")
                    try:
                        filtru_pret = int(filtru_pret)
                        self.change_filter(filtru_nume, filtru_pret)
                    except ValueError:
                        print("nu este intreg!")
                case "4":
                    try:
                        self.Controller.undo()
                    except ValueError:
                        print("Nu se mai poate da inapoi!")
                case _:
                    print("input invalid")


    def get_all_filtered(self):
        """
        Returneaza toate tractoarele dupa filtru
        :return: lista de tractoare ce indepl cond
        """
        return self.Controller.get_all_filtered()

    def adauga_tractor(self, tractor):
        """
        adauga tractorul tractor in tractoare
        :param tractor: tractor, tractorul de adaugat
        :return: None
        """
        self.Controller.adauga_tractor(tractor)

    def sterge_tractoare(self, price):
        """
        Sterge tractoare
        :param price: cifra dupa care sterge
        :return: None
        """
        return self.Controller.sterge_tractoare(price)

    def change_filter(self, filtru_denumire, filtru_pret):
        """
        Schimbare filtru
        :param filtru_denumire: filtru denumire nou
        :param filtru_pret: filtru pret nou
        :return: None
        """
        return self.Controller.change_filter(filtru_denumire, filtru_pret)