from Domain.entities import Species
from Repository.file_repository import SpeciesRepository

class SpeciesController():
    """
    Controller pentru gestionarea speciilor
    """
    def __init__(self, file_name):
        """
        Initializarea controllerului cu numele fisierului din care se vor prelua datele
        :param file_name: str, numele fisierului
        """
        self.repository = SpeciesRepository(file_name)

    def get_earlier_than(self, date):
        """
        Returneaza toate animalele care au fost descoperite la o data anterioara celei date
        :param date: data maxima
        :return: dict cu cele gasite
        """
        result = {}

        for animal in self.repository.get_all().values():
            current_date = animal.get_date()
            if current_date <= date:
                result[animal.get_id()] = animal

        return result.values()

    def get_statistics(self):
        """
        Returneza statisticile pentru fiecare animal din repo
        :return:
        """
        report = []
        types = self.repository.get_types()
        for type in types:
            max_date = "0000/00/00"

            found = 0
            for animal in self.repository.get_species_by_type(type).values():
                date = animal.get_date()

                if date >= max_date:
                    max_date = date
                    latest_animal = animal
                    found = 1

            if found == 1:
                total = 0
                count = 0
                for animal in self.repository.get_species_by_type(type).values():
                    total = total + animal.get_lifespan()
                    count = count + 1

                total = total/count

                result = (type, latest_animal.get_name(), total)

                report.append(result)

        return report


def test_controller_species():
    controller = SpeciesController("test_species.txt")
    assert controller.get_statistics()[0] == ("mammal", "Bober",22.0)

    assert len(controller.get_earlier_than("2023/99/99")) == 10

test_controller_species()
