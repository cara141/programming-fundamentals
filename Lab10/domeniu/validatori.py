from domeniu.obiecte import Student
from domeniu.obiecte import Disciplina
from domeniu.obiecte import NotaStudent

class ExceptieCRUD(Exception):
    pass

class ExceptieValidare(ExceptieCRUD):
    def __init__(self, mesaje):
        """
        Initializare exceptie de vaidare
        :param mesaje: lista de siruri de caractere (erorile)
        """
        self.__mesaje = mesaje

    def get_mesaje(self):
        """
        Metoda getter pentru mesaje
        :return: lista de mesaje de eroare
        """
        return self.__mesaje

    def __str__(self):
        """
        Reprezentare sir de caractere a exceptiei de validare
        :return: sir de caractere ce contine toate mesajele de eroare
        """
        return str(self.__mesaje)

class ValidatorStudent:
    def __init__(self):
        """
        Clasa responsabila cu validarea studentilor
        """
        pass

    def valideaza(self, student):
        """
        Validare __student
        :param student: studentul de validat
        :return: arunca ExceptieValidare daca id, nume sau adresa sunt goale
        """
        mesaje_de_eroare = []
        if student.get_id() == "":
            mesaje_de_eroare.append("Id nu poate fi gol \n")
        if student.get_nume() == "":
            mesaje_de_eroare.append("Nume nu poate fi gol \n")

        if mesaje_de_eroare != []:
            raise ExceptieValidare(mesaje_de_eroare)

def test_validare_student():
    """
    Testare metoda de validare
    Functionalitate 1 - adauga __student
    Activitate 2 - valideaza __student
    """

    validator = ValidatorStudent()
    student = Student("", "Cezar")
    try:
        validator.valideaza(student)
        assert False
    except ExceptieValidare:
        assert True

    student = Student(1, "")
    try:
        validator.valideaza(student)
        assert False
    except ExceptieValidare:
        assert True

test_validare_student()

class ValidatorDisciplina():
    def __init__(self):
        """
        Clasa responsabila cu validarea disciplinelor
        """
        pass

    def valideaza(self, disciplina):
        """
        Valideaza __disciplina
        :param disciplina: __disciplina de validat
        :return: None
        """
        mesaje_de_eroare = []
        if disciplina.get_id() == "":
            mesaje_de_eroare.append("ID __disciplina nu poate fi gol.")
        if disciplina.get_nume() == "":
            mesaje_de_eroare.append("Nume nu poate fi gol.")
        if disciplina.get_profesor() == "":
            mesaje_de_eroare.append("Profesor __disciplina nu poate fi gol")

        if mesaje_de_eroare != []:
            raise ExceptieValidare(mesaje_de_eroare)

def test_validare_disciplina():
    """
    Metoda de testare pentru validare
    Functionalitate 2 - adauga __disciplina
    Activitate 4 - validare __disciplina
    """
    validator = ValidatorDisciplina()
    disciplina = Disciplina("", "FP", "Czibula")
    try:
        validator.valideaza(disciplina)
        assert False
    except ExceptieValidare:
        assert True

    disciplina = Disciplina(1, "", "Czibula")
    try:
        validator.valideaza(disciplina)
        assert False
    except ExceptieValidare:
        assert True

    disciplina = Disciplina(1, "FP", "")
    try:
        validator.valideaza(disciplina)
        assert False
    except ExceptieValidare:
        assert True

test_validare_disciplina()

class ValidatorNota:
    def __init__(self):
        """
        Metoda pentru validarea notelor
        """
        pass

    def valideaza(self, nota):
        """
        Valideaza nota
        :param nota: nota = nota de validat
        :return: None
        arunca ExceptieValidare daca scorul nu este intre 0 si 10
        """
        if nota.get_scor() <= 0 or nota.get_scor() > 10:
            raise ExceptieValidare("Nota trebuie sa fie intre 0 si 10.")

def test_validare_nota():
    student = Student(1, "Cezar")
    disciplina = Disciplina(1, "Analiza", "Berinde")
    nota = NotaStudent(1, student.get_id(), disciplina.get_id(), 101)
    validator = ValidatorNota()
    try:
        validator.valideaza(nota)
        assert False
    except ExceptieValidare:
        assert True

test_validare_nota()

