from Domain.entities import Tractor
from Repository.repository import TractorRepository

class TractorController():
    """
    Controller pentru tractor
    """
    def __init__(self, nume_fisier):
        """
        Initializare controller tractor
        :param nume_fisier: numele fisierului din care trage
        """
        self.Repo = TractorRepository(nume_fisier)

    def adauga_tractor(self, tractor):
        """
        adauga tractor
        :param tractor: tractorul de adaugat
        :return: None
        """
        self.Repo.adauga_tractor(tractor)

    def sterge_tractoare(self, price):
        """
        Stergeti tractoarele
        :param price: cifra
        :return: Numarul de tractoare sterse
        """
        return self.Repo.sterge_tractoare(price)

    def undo(self):
        """
        Reface repo
        :return: None
        """
        self.Repo.undo()

    def get_all_filtered(self):
        """
        Preia toate tractoarele dupa filtru
        :return: Taote tractoarele ce indeplinesc conditiile
        """
        return self.Repo.get_all_filtered()

    def change_filter(self, filtru_denumire,filtru_pret):
        """
        schimba filtru
        :param filtru_denumire: str filtru nou denumire
        :param filtru_pret: int filtru nou pret
        :return: None
        """
        self.Repo.change_filter(filtru_denumire, filtru_pret)

def test_controller():
    file_name = "test_tractor.txt"
    Controller = TractorController(file_name)
    assert len(Controller.Repo.tractoare) == 10
    tractor = Tractor(1, "tractor1", 10, "A", "01:10:2024")
    try:
        Controller.adauga_tractor(tractor)
        assert False
    except ValueError:
        assert True

    try:
        Controller.undo()
        assert False
    except ValueError:
        assert True

    assert (Controller.sterge_tractoare(0)) == 2
    tractor = Tractor(1, "tractor1", 10, "A", "01:10:2024")
    Controller.adauga_tractor(tractor)
    tractor = Tractor(2, "tractor1", 10, "A", "01:10:2024")
    Controller.adauga_tractor(tractor)
    assert (Controller.sterge_tractoare(9)) == 0
test_controller()