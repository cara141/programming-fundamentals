import datetime
class Tractor():
    """
    Retine date despre tractor
    """
    def __init__(self, id, name, price, model, date):
        """
        Init tractor
        :param id: int, id
        :param name: str, denumire
        :param price: int, pret
        :param model: str, model
        :param date: str, data
        """
        self.id = id
        self.name = name
        self.price = price
        self.model = model
        self.date = date

    def get_id(self):
        """
        Id tractor
        :return: int, id tractor
        """
        return self.id

    def get_name(self):
        """
        Nume tractor
        :return: str, nume tractor
        """
        return self.name

    def get_price(self):
        """
        Pret tractor
        :return: int, pretul tractorului
        """
        return self.price

    def get_model(self):
        """
        Model tractor
        :return: str, modelul tractorului
        """
        return self.model

    def get_date(self):
        """
        data expirarii tractorului
        :return: str, data expirarii
        """
        return self.date

    def __str__(self):
        current_day = datetime.date.today().day
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year

        aux = self.date
        aux = aux.split(':')

        day = int(aux[0])
        month = int(aux[1])
        year = int(aux[2])

        if year >= current_year:
            return (f"{self.id}, {self.name}, {self.price}, {self.model}, {self.date}")
        elif month < current_month:
            return (f"{self.id}, *{self.name}, {self.price}, {self.model}, {self.date}")
        elif day < current_day:
            return (f"{self.id}, *{self.name}, {self.price}, {self.model}, {self.date}")

        if month >= current_month:
            return (f"{self.id}, {self.name}, {self.price}, {self.model}, {self.date}")
        elif day < current_day:
            return (f"{self.id}, *{self.name}, {self.price}, {self.model}, {self.date}")

        if day >= current_day:
            return (f"{self.id}, {self.name}, {self.price}, {self.model}, {self.date}")



def test_tractor():
    tractor = Tractor(1,"tractor1", 10, "A", "10:10:2024")
    assert tractor.get_id() == 1
    assert tractor.get_name() == "tractor1"
    assert tractor.get_price() == 10
    assert tractor.get_model() == "A"
    assert tractor.get_date() == "10:10:2024"

test_tractor()