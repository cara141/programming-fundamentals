class SpeciesCRUDException(Exception):
    pass


class Species:
    """
    clasa pentru specii

    """
    def __init__(self, species_id, name, date, location, species_type, lifespan):
        """
        Initializare clasa specii, se va init cu datele necesare
        :param species_id: int, id specie
        :param name: str, nume specie
        :param date: str, data descoperirii
        :param location: str , locatia
        :param species_type: str, tipul, reptile, insect, bird
        :param lifespan: str , durata de viata in ani
        """
        self.__id = species_id
        self.__name = name
        self.__date = date
        self.__location = location
        self.__type = species_type
        self.__lifespan = lifespan

    def __str__(self):
        """
        Afisarea unei specii cu datele necesare
        :return: "<id>,<nume>,<data>,<locatie>,<tip>,<lifespan>"
        """
        print(str(self.__id)+" "+self.__name+" "+self.__date+" "+self.__location+" "+self.__type+" "+
              str(self.__lifespan))

    def get_id(self):
        """
        getter pentru id
        :return: id, int
        """
        return self.__id

    def get_name(self):
        """
        getter pentru nume
        :return: name, str
        """
        return self.__name

    def get_date(self):
        """
        getter pentru data descoperirii
        :return: date, str
        """
        return self.__date

    def get_location(self):
        """
        getter pentru locatie
        :return: location, str
        """
        return self.__location

    def get_type(self):
        """
        getter pentru tipul speciei
        :return: type, str
        """
        return self.__type

    def get_lifespan(self):
        """
        Getter pentru durata de viata
        :return: lifespan, int
        """
        return self.__lifespan


def test_species():
    """
    Test function for species
    :return: None.
    """
    species = Species(1,"Bober","2023/12/12","Poland","mammal",10)
    assert species.get_lifespan() == 10
    assert species.get_name() == "Bober"
    assert species.get_location() == "Poland"
    assert species.get_type() == "mammal"
    assert species.get_id() == 1
    assert species.get_date() == "2023/12/12"

test_species()