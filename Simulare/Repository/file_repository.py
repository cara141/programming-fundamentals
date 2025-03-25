from Domain.entities import Species

class SpeciesRepository():
    """
    Repository pentru clasa speciilor de animale
    """
    def __init__(self, file_name):
        """
        Initializare repository cu date din fisier
        """
        self.__file_name = file_name
        self.__species = {}
        self.__load_from_file()

    def size(self):
        """
        Determina numele speciilor din repo
        :return: size, int
        """
        return len(self.__species)

    def get_all(self):
        """
        Returneaza toate speciile din repo
        :return: __species, dict of species
        """
        return self.__species

    def get_species_by_type(self, type):
        """
        Returneaza dictionarul cu toate speciile din repo care au acel tip.
        :param type: tipul dupa care se cauta
        :return: result, dictionar cu toate speciile gasite
        """
        result = {}
        for animal in self.__species.values():
            if animal.get_type() == type:
                result[animal.get_id()] = animal
        return result

    def get_types(self):
        """
        Returneaza lista cu toate tipurile de specii din repo
        :return: types, lista de str
        """
        types = []
        for animal in self.__species.values():
            if animal.get_type() in types:
                pass
            else:
                types.append(animal.get_type())
        return types

    def __load_from_file(self):
        """
        Preia toate datele despre specii din fisier si le pune in repo
        :return: None.
        """
        try:
            file = open(self.__file_name, "r")
        except IOError:
            print("Nu se poate deschide fisierul")
            return

        line = file.readline().strip()
        while line != "":
            line = line.split(",")
            species_id = int(line[0])
            name = line[1]
            date = line[2]
            location = line[3]
            species_type = line[4]
            lifespan = int(line[5])
            species = Species(species_id, name, date, location, species_type, lifespan)
            self.__species[species.get_id()] = species
            line = file.readline().strip()
        file.close()

    def __save_to_file(self):
        try:
            file = open(self.__file_name, "w")
        except IOError:
            print("Nu se poate deschide fisierul")
            return

        for animal in self.__species:
            animal_string = str(animal.get_id())+","
            animal_string = animal_string + animal.get_name() + ","
            animal_string = animal_string + animal.get_date() + ","
            animal_string = animal_string + animal.get_location() + ","
            animal_string = animal_string + animal.get_type() + ","
            animal_string = animal_string + animal.get_lifespan() + ",\n"

            file.write(animal_string)
        file.close()


def test_repo_species():
    """
    Test function for species repositroy
    :return: None.
    """
    repository = SpeciesRepository("test_species.txt")
    assert repository.size() == 10
    assert len(repository.get_all()) == 10
    assert len(repository.get_species_by_type("mammal")) == 5
    assert len(repository.get_types()) == 4

test_repo_species()
