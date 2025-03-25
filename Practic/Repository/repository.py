from Domain.entities import Tractor
import copy

class TractorRepository():
    """
    Repo Tractor :3
    """
    def __init__(self, nume_fisier):
        """
        initializare
        :param nume_fisier: str, numele fisierului de unde isi trage si stocheaza datele
        """
        self.nume_fisier = nume_fisier
        self.tractoare = {}
        self.load_from_file()
        self.undoStack = []
        self.filtru_denumire = ""
        self.filtru_pret = -1

    def save_to_file(self):
        """
        actuazlizare  fisier
        :return: None
        """
        try:
            file = open(self.nume_fisier, "w")
        except IOError:
            return
        for tractor in self.tractoare.values():
            linie_fisier = str(tractor.get_id()) + ','
            linie_fisier = linie_fisier + tractor.get_name() + ','
            linie_fisier = linie_fisier + str(tractor.get_price()) + ','
            linie_fisier = linie_fisier + tractor.get_model() + ','
            linie_fisier = linie_fisier + tractor.get_date() + '\n'
            file.write(linie_fisier)
        file.close()

    def change_filter(self, name_filter, price_filter):
        """
        Schimba filtru
        :param name_filter: str, nume filtru
        :param price_filter: int, pret filtru
        :return: None
        """
        self.filtru_pret = price_filter
        self.filtru_denumire = name_filter

    def get_all_filtered(self):
        """
        returneaza toate tractoarele dupa filtru
        :return: aux, list, toate tractoarele
        """
        aux = []
        for tractor in self.tractoare.values():
            if self.filtru_denumire in tractor.get_name():
                if self.filtru_pret == -1:
                    aux.append(tractor)
                elif self.filtru_pret >= tractor.get_price():
                    aux.append(tractor)
        return aux

    def load_from_file(self):
        """
        actualizeaza repo cu val din fisier
        :return: None
        """
        try:
            file = open(self.nume_fisier, "r")
        except IOError:
            return
        line = file.readline().strip()
        while len(line) > 1:
            line = line.split(',')
            id = int(line[0])
            name = line[1]
            price = int(line[2])
            model = line[3]
            date = line[4]
            tractor = Tractor(id, name, price, model, date)
            self.tractoare[id] = tractor
            line = file.readline().strip()
        file.close()

    def update_undoStack(self):
        """
        update undo stack
        :return: None
        """

        self.undoStack.append(copy.deepcopy(self.tractoare))

    def undo(self):
        """
        reface ultima operatie
        :return: None
        """
        if len(self.undoStack) == 0:
            raise ValueError()
        else:
            self.tractoare = self.undoStack.pop()

    def adauga_tractor(self, tractor):
        """
        adauga tractor in repo
        :param tractor: tractorul de adaugat
        :return: None
        :raise: ValueError() if tractor is in repo
        """
        if tractor.get_id() in self.tractoare:
            raise ValueError()
        else:
            self.update_undoStack()
            self.tractoare[tractor.get_id()] = tractor
            self.save_to_file()


    def sterge_tractoare(self, price):
        """
        sterge tractoarele care au cifra price in pretul lor
        :param price: cifra care apare in pret
        :return: cate tractoare s-au sters
        :raise: ValueError repo e gol
        """
        if(len(self.tractoare) == 0):
            raise ValueError("nu se mai poate sterge!")
        de_sters = []
        tractoare = (self.tractoare.values())
        for tractor in tractoare:
            pret = tractor.get_price()
            while pret != 0:
                c = pret % 10
                pret = pret // 10
                if c == price:
                    de_sters.append(tractor.get_id())
                    break

        for ids in de_sters:
            self.tractoare.pop(ids)

        self.update_undoStack()
        self.save_to_file()
        self.update_undoStack()
        return len(de_sters)

def test_repositroy():
    file_name = "test_tractor.txt"
    Repo = TractorRepository(file_name)
    assert len(Repo.tractoare) == 10
    tractor = Tractor(1, "tractor1", 10, "A", "01:10:2024")
    try:
        Repo.adauga_tractor(tractor)
        assert False
    except ValueError:
        assert True

    try:
        Repo.undo()
        assert False
    except ValueError:
        assert True

    assert(Repo.sterge_tractoare(0)) == 2
    tractor = Tractor(1, "tractor1", 10, "A", "01:10:2024")
    Repo.adauga_tractor(tractor)
    tractor = Tractor(2, "tractor1", 10, "A", "01:10:2024")
    Repo.adauga_tractor(tractor)
    assert(Repo.sterge_tractoare(9)) == 0
test_repositroy()