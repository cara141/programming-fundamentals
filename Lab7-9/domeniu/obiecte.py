class Student:
    """
    Reprezinta un __student
    """
    def __init__(self, id, nume):
        """
        Creeaza un __student nou
        :param id: numar intreg
        :param nume: sir de caractere
        """
        self.__id = id
        self.__nume = nume

    def get_id(self):
        """
        Metoda de getter pentru id
        :return: id ul studentului
        """
        return self.__id

    def set_id(self, id_nou):
        """
        Metoda de setter pentru id (irelevanta, id-ul nu se va modifica niciodata
        :param id_nou: noul id al studentului
        :return: None.
        """
        self.__id = id_nou

    def get_nume(self):
        """
        Metoda getter pentru nume
        :return: numele studentului
        """
        return self.__nume

    def set_nume(self, nume_nou):
        """
        Metoda setter pentru nume
        :param nume_nou: numele nou al disciplinei
        :return: None.
        """
        self.__nume = nume_nou

    def __str__(self):
        """
        Reprezentare a studentului sub forma de sir de caractere
        :return: string ce contine toate atributele studentului
        """
        return f"Student cu numele {self.__nume} si id {self.__id}"

    def __eq__(self, altul):
        """
        Definitie identitate intre instante de studenti
        :param altul: alta instanta de __student
        :return: True, daca altul si studentul au acelasi id, False, in caz contrar
        """

        if altul == None:
            return False
        return self.__id == altul.__id

def test_identitate_student():
    student_1 = Student(1, "Cezar")
    student_2 = Student(1, "Cezar")
    assert student_2 == student_1

    student_1 = Student(1, "Cezar")
    student_2 = Student(2, "Ioana")
    assert student_2 != student_1

test_identitate_student()

def test_student():
    """
    Testare creeare __student
    Functionalitate 1 - adaugare __student
    Activitate 1 - Creeare __student
    """

    student = Student(1, "Cezar")
    assert student.get_id() == 1
    assert student.get_nume() == "Cezar"

    student.set_id(2)
    student.set_nume("Ioana")
    assert student.get_id() == 2
    assert student.get_nume() == "Ioana"

test_student()

class Disciplina:
    """
    Reprezinta o __disciplina
    """
    def __init__(self, id, nume, profesor):
        """
        Creeaza o __disciplina
        :param id: numar intreg, id ul disciplinei
        :param nume: sir de caractere, numele disciplinei
        :param profesor: sir de caractere, numele profesorului
        """
        self.__id = id
        self.__nume = nume
        self.__profesor = profesor

    def get_id(self):
        """
        Metoda getter pentru id
        :return: id ul disciplinei, numar intreg
        """
        return self.__id

    def set_id(self, id_nou):
        """
        Metoda setter pentru id
        :param id_nou: noul id al disciplinei, numar intreg
        :return: None.
        """
        self.__id = id_nou

    def get_nume(self):
        """
        Metoda getter pentru nume
        :return: numele disciplinei, sir de caractere
        """
        return self.__nume

    def set_nume(self, nume_nou):
        """
        Metoda setter pentru nume
        :param nume_nou: Noul nume al disciplinei, sir de caractere
        :return: None.
        """
        self.__nume = nume_nou

    def get_profesor(self):
        """
        Metoda getter pentru profesor
        :return: Numele profesorului disciplinei respective, sir de caractere
        """
        return self.__profesor

    def set_profesor(self, profesor_nou):
        """
        Metoda setter pentru profesor
        :param profesor_nou: Noul nume al profesorului disciplinei, sir de caractere
        :return: None.
        """
        self.__profesor = profesor_nou

    def __eq__(self, altul):
        """
        Definitie identitate intre doua instante tip __disciplina
        :param altul: alta instanta tip __disciplina
        :return: True, doua discipline cu acelasi id, False, caz contrar
        """
        if altul == None:
            return False
        else:
            return self.__id == altul.__id

    def __str__(self):
        """
        Reprezentare a disciplinei sub forma de sir de caracter
        :return: Sir de caractere ce contine toate atributele studentului
        """
        return f"Disciplina {self.__nume}, cu titular de curs {self.__profesor} si id {self.__id}"

def test_disciplina():
    disciplina = Disciplina(1, "FP", "Czibula")
    assert disciplina.get_id() == 1
    assert disciplina.get_nume() == "FP"
    assert disciplina.get_profesor() == "Czibula"

    disciplina.set_id(2)
    disciplina.set_nume("Analiza matematica")
    disciplina.set_profesor("Berinde")
    assert disciplina.get_id() == 2
    assert disciplina.get_nume() == "Analiza matematica"
    assert disciplina.get_profesor() == "Berinde"

test_disciplina()

def test_identitate_disciplina():
    disciplina_1 = Disciplina(1, "FP", "Czibula")
    disciplina_2 = Disciplina(1, "FP", "Czibula")
    assert disciplina_1 == disciplina_2

test_identitate_disciplina()

class NotaStudent:
    """
    Obiect de Transfer de Date
    """
    def __init__(self, id_nota, id_student, id_disciplina, scor):
        self.__id_nota = id_nota
        self.__id_student = id_student
        self.__id_disciplina = id_disciplina
        self.__scor = scor
        self.__student = None
        self.__disciplina = None

    def get_id_nota(self):
        """
        Metoda getter pentru id ul notei
        :return: numar intreg, id ul notei
        """
        return self.__id_nota

    def get_id_student(self):
        """
        Metoda getter pentru id ul studentului
        :return: numar intreg, id ul studentului
        """
        return self.__id_student

    def get_id_disciplina(self):
        """
        Metoda getter pentru id ul disciplinei
        :return: numar intreg, id ul disciplinei
        """
        return self.__id_disciplina

    def get_scor(self):
        """
        Metoda getter pentru scorul notei
        :return: numar real, scorul notei
        """
        return self.__scor

    def set_id_nota(self, id_nota_nou):
        """
        Metoda setter pentru id ul notei
        :param id_nota_nou: numar intreg, noul id al notei
        :return: None.
        """
        self.__id_nota = id_nota_nou

    def set_id_student(self, id_student_nou):
        """
        Metoda setter pentru id ul studentului notei
        :param id_student_nou: numar intreg, noul id al studentului
        :return: None
        """
        self.__id_student = id_student_nou

    def set_id_disciplina(self, id_disciplina_nou):
        """
        Metoda setter pentru id ul disciplinei notei
        :param id_disciplina_nou: numar intreg, noul id al disciplinei
        :return: None
        """
        self.__id_disciplina = id_disciplina_nou

    def set_scor(self, scor_nou):
        """
        Metoda setter pentru scorul notei
        :param scor_nou: numar real, noul scor al notei
        :return: None.
        """
        self.__scor = scor_nou

    def get_student(self):
        """
        Metoda getter pentru student
        :return: referinta la studentul din nota
        """
        return self.__student

    def get_disciplina(self):
        """
        Metoda getter pentru disciplina
        :return: referinta la disciplina din nota
        """
        return self.__disciplina

    def set_student(self, student):
        """
        Metoda setter pentru studentul din nota
        :param student: referinta la studentul din nota
        :return: None
        """
        self.__student = student

    def set_disciplina(self, disciplina):
        """
        Metoda setter pentru disciplina din nota
        :param disciplina: referinta la disciplina din nota
        :return: None
        """
        self.__disciplina = disciplina

    def __eq__(self, altul):
        """
        Defineste identitatea intre doua instante de tip nota
        :param altul: alta instanta de tip nota
        :return: True, cele doua note au acelasi id de nota, False, contrar
        """
        if altul == None:
            return False
        else:
            return self.__id_nota == altul.__id_nota

    def __str__(self):
        """
        Reprezentare sir de caractere a notei unui __student
        :return: Sir de caractere ce contine toate datele despre nota
        """
        return f"{self.__student} la {self.__disciplina} a obtinut nota {self.__scor}"

def test_nota():
    nota = NotaStudent(1, 1, 1, 9.25)
    assert nota.get_id_nota() == 1
    assert nota.get_id_student() == 1
    assert nota.get_id_disciplina() == 1
    assert nota.get_scor() == 9.25

    nota.set_id_nota(2)
    nota.set_id_student(2)
    nota.set_id_disciplina(2)
    nota.set_scor(10)

    assert nota.get_id_nota() == 2
    assert nota.get_id_student() == 2
    assert nota.get_id_disciplina() == 2
    assert nota.get_scor() == 10

test_nota()

def test_identitate_nota():
    nota_1 = NotaStudent(1, 1, 1, 9.25)
    nota_2 = NotaStudent(1, 1, 1, 9.25)
    assert nota_1 == nota_2

test_identitate_nota()

