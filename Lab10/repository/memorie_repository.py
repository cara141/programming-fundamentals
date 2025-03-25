from domeniu.obiecte import Student
from domeniu.obiecte import Disciplina
from domeniu.obiecte import NotaStudent
from domeniu.validatori import ExceptieCRUD

class ExceptieRepository(ExceptieCRUD):
    """
    Clasa de baza pentru exceptiile in repository
    """

    def __init__(self, mesaje_de_eroare):
        """
        Initializare exceptie repository
        :param mesaje_de_eroare: lista de siruri de caractere ce reprezinta
        mesaje de eroare
        """
        self.__mesaje_de_eroare = mesaje_de_eroare

    def get_mesaje(self):
        """
        Metoda getter pentru mesaje de eroare
        :return: lista de mesaje de eroare
        """
        return self.__mesaje_de_eroare

    def __str__(self):
        return str(self.__mesaje_de_eroare)


class ExceptieIDDuplicat(ExceptieRepository):
    def __init__(self):
        ExceptieRepository.__init__(self, "ID Duplicat")

class RepositoryStudent:
    """
    Clasa responsabila pentru operatiile CRUD pe lista de studenti
    """
    def __init__(self):
        self.__studenti = {}

    def stocare(self, student):
        """
        Stocare student
        :param student: instanta student de stocat
        :return: None
        arunca ExceptieIDDuplicat pentru id duplicat
        """

        if student.get_id() in self.__studenti:
            raise ExceptieIDDuplicat()
        self.__studenti[student.get_id()] = student

    def dimensiune(self):
        """
        Metoda read pentru dimensiunea listei de studenti
        :return: lungimea listei de studenti
        """
        return len(self.__studenti)

    def elimina(self, id_student):
        """
        elimina un student din repository
        :param id_student: numar intreg, id ul studentului de eliminat
        :return: studentul eliminat
        arunca ValueError daca nu este un student cu id ul dat
        """
        if not id_student in self.__studenti:
            raise ValueError(f"Nu exista studentul cu id {id_student}")
        student = self.__studenti[id_student]
        del self.__studenti[id_student]
        return student

    def elimina_tot(self):
        """
        elimina toti studenti din repository
        :return: None
        """
        self.__studenti = {}

    def get_toti(self):
        """
        Obtine toti studentii
        :return: lista de studenti in intregime
        """
        return self.__studenti

    def update(self, id_student, student_nou):
        """
        Metoda update pentru student
        :param id_student: id ul studentului de eliminat
        :param student_nou: noul student
        :return: None.
        arunca ValueError daca nu exista student cu id ul dat
        """

        self.elimina(id_student)
        self.stocare(student_nou)

    def gaseste(self, id_student):
        """
        Cauta studentul cu id ul dat
        :param id_student: numar intreg, id ul studentului de cautat
        :return: studentul daca este gasit sau None, in caz contrar
        """
        if not id_student in self.__studenti:
            return None
        return self.__studenti[id_student]

def test_stocare_student():
    """
    Test functie de stocare student
    Functionalitate 1 - adauga student
    Activitate 3 - stocheaza student
    """

    student = Student(1, "Cezar")
    repository = RepositoryStudent()
    assert repository.dimensiune() == 0

    repository.stocare((student))
    assert repository.dimensiune() == 1

    student = Student(2, "Ioana")
    repository.stocare(student)
    assert repository.dimensiune() == 2

    student = Student(1, "Cristina")
    try:
        repository.stocare(student)
        assert False
    except ExceptieIDDuplicat:
        assert True

test_stocare_student()

def test_eliminare_student():
    """
    Functie de test pentru eliminare student
    Functionalitate 2 - stergere student
    Activitate 1 - sterge student din repository
    """

    repository = RepositoryStudent()
    student = Student(1, "Cezar")
    repository.stocare(student)
    student = Student(2, "Ioana")
    repository.stocare(student)
    student = Student(3, "Cristina")
    repository.stocare(student)

    assert repository.dimensiune() == 3
    repository.elimina(1)
    assert repository.dimensiune() == 2

    try:
        repository.elimina(5)
        assert False
    except ValueError:
        assert True

test_eliminare_student()

def test_listeaza_studenti():
    """
    Functie de test pentru get_toti
    Functionalitate 3 - listeaza toti studenti dupa criteriu
    Activitate 1 - returneaza toti studenti din repository
    """

    repository = RepositoryStudent()

    student = Student(1, "Cezar")
    repository.stocare(student)
    student = Student(2, "Ioana")
    repository.stocare(student)
    student = Student(3, "Cristina")
    repository.stocare(student)

    toti = repository.get_toti()
    assert len(toti) == 3
    student1 = repository.gaseste(1)
    assert student1.get_id() == 1
    assert student1.get_nume() == "Cezar"
    student2 = repository.gaseste(2)
    assert student2.get_id() == 2
    assert student2.get_nume() == "Ioana"


test_listeaza_studenti()

def test_update_student():
    """
    Functie de test pentru update
    Functionalitate 4 - modifica informatiile despre un student
    Activitate 1 - modifica student in repository
    """

    repository = RepositoryStudent()

    student = Student(1, "Cezar")
    repository.stocare(student)
    student = Student(1, "Ioana")
    repository.update(1, student)
    assert repository.gaseste(1).get_nume() == "Ioana"

test_update_student()


class RepositoryDisciplina:
    """
    Clasa responsabila pentru operatiile CRUD pe lista de discipline
    """
    def __init__(self):
        self.__discipline = {}

    def stocare(self, disciplina):
        """
        Stocare disciplina
        :param disciplina: instanta disciplina de stocat
        :return: None
        arunca ExceptieIDDuplicat pentru id duplicat
        """

        if disciplina.get_id() in self.__discipline:
            raise ExceptieIDDuplicat()
        self.__discipline[disciplina.get_id()] = disciplina

    def dimensiune(self):
        """
        Metoda read pentru dimensiunea listei de discipline
        :return: lungimea listei de discipline
        """
        return len(self.__discipline)

    def elimina(self, id_disciplina):
        """
        elimina o disciplina din repository
        :param id_disciplina: numar intreg, id ul disciplinei de eliminat
        :return: disciplina eliminata
        arunca ValueError daca nu este o disciplina cu id ul dat
        """
        if not id_disciplina in self.__discipline:
            raise ValueError(f"Nu exista studentul cu id {id_disciplina}")
        disciplina = self.__discipline[id_disciplina]
        del self.__discipline[id_disciplina]
        return disciplina

    def elimina_tot(self):
        """
        elimina toate disciplinele din repository
        :return: None
        """
        self.__discipline = {}

    def get_toti(self):
        """
        Obtine toate disciplinele
        :return: lista de discipline in intregime
        """
        return self.__discipline

    def update(self, id_disciplina, disciplina_noua):
        """
        Metoda update pentru disciplina
        :param id_disciplina: id ul disciplinei de eliminat
        :param disciplina_noua: noua disciplina
        :return: None.
        arunca ValueError daca nu exista disciplina cu id ul dat
        """

        self.elimina(id_disciplina)
        self.stocare(disciplina_noua)

    def gaseste(self, id_disciplina):
        """
        Cauta disciplina cu id ul dat
        :param id_disciplina: numar intreg, id ul disciplinei de cautat
        :return: disciplina daca este gasit sau None, in caz contrar
        """
        if not id_disciplina in self.__discipline:
            return None
        return self.__discipline[id_disciplina]

def test_stocare_disciplina():
    """
    Test functie de stocare disciplina
    Functionalitate 4 - adauga disciplina
    Activitate 3 - stocheaza disciplina
    """

    disciplina = Disciplina(1, "FP", "Czibula")
    repository = RepositoryDisciplina()
    assert repository.dimensiune() == 0

    repository.stocare(disciplina)
    assert repository.dimensiune() == 1

    disciplina = Disciplina(2, "Analiza", "Berinde")
    repository.stocare(disciplina)
    assert repository.dimensiune() == 2

    disciplina = Disciplina(1, "Algebra", "Modoi")
    try:
        repository.stocare(disciplina)
        assert False
    except ExceptieIDDuplicat:
        assert True

test_stocare_disciplina()

def test_eliminare_disciplina():
    """
    Functie de test pentru eliminare disciplina
    Functionalitate 5 - stergere disciplina
    Activitate 1 - sterge disciplina din repository
    """

    repository = RepositoryDisciplina()
    disciplina = Disciplina(1, "FP", "Czibula")
    repository.stocare(disciplina)
    disciplina = Disciplina(2, "Analiza", "Berinde")
    repository.stocare(disciplina)
    disciplina = Disciplina(3, "Algebra", "Modoi")
    repository.stocare(disciplina)

    assert repository.dimensiune() == 3
    repository.elimina(1)
    assert repository.dimensiune() == 2

    try:
        repository.elimina(5)
        assert False
    except ValueError:
        assert True

test_eliminare_disciplina()

def test_listeaza_discipline():
    """
    Functie de test pentru get_toti
    Functionalitate 3 - listeaza toate disciplinele dupa criteriu
    Activitate 1 - returneaza toate disciplinele din repository
    """

    repository = RepositoryDisciplina()
    disciplina = Disciplina(1, "FP", "Czibula")
    repository.stocare(disciplina)
    disciplina = Disciplina(2, "Analiza", "Berinde")
    repository.stocare(disciplina)
    disciplina = Disciplina(3, "Algebra", "Modoi")
    repository.stocare(disciplina)

    toti = repository.get_toti()
    assert len(toti) == 3
    disciplina1 = repository.gaseste(1)
    assert disciplina1.get_id() == 1
    assert disciplina1.get_nume() == "FP"
    assert disciplina1.get_profesor() == "Czibula"
    disciplina2 = repository.gaseste(2)
    assert disciplina2.get_id() == 2
    assert disciplina2.get_nume() == "Analiza"
    assert disciplina2.get_profesor() == "Berinde"


test_listeaza_discipline()

def test_update_disciplina():
    """
    Functie de test pentru update
    Functionalitate 4 - modifica informatiile despre un __student
    Activitate 1 - modifica __student in repository
    """

    repository = RepositoryDisciplina()
    disciplina = Disciplina(1, "FP", "Czibula")
    repository.stocare(disciplina)
    disciplina = Disciplina(1, "Analiza", "Berinde")
    repository.update(1, disciplina)
    assert repository.gaseste(1).get_nume() == "Analiza"

test_update_disciplina()

class RepositoryNoteStudent:
    """
    Repository pentru note studenti
    Notele sunt salvate in memorie
    """

    def __init__(self):
        self.__note = {}

    def stocare(self, nota):
        """
        Stocheaza o nota
        :param nota: nota de stocat
        :return: None
        """

        if nota.get_id_nota() in self.__note:
            raise ExceptieIDDuplicat()
        self.__note[nota.get_id_nota()] = nota

    def dimensiune(self):
        """
        :return: numarul de note in repository
        """
        return len(self.__note)

    def gaseste(self, id_nota):
        """
        Cauta nota dupa id ul sau
        :param id_nota: id ul notei
        :return: Nota sau None daca nu exista
        """
        if id_nota not in self.__note:
            return None
        else:
            return self.__note[id_nota]

    def get_toti(self):
        """
        Metoda read pentru toate notele din repository
        :return: toate notele din repository
        """
        return self.__note

    def elimina_tot(self):
        self.__note = {}

    def get_toti_dupa_student(self, id_student):
        """
        Metoda read pentru toate notele din repository care au fost obtinute de student
        :param id_student: id ul studentului pentru care se cauta notele
        :return: lista cu toate notele obtinute de student
        """
        rezultat = []
        for nota in self.get_toti().values():
            if nota.get_id_student() == id_student:
                rezultat.append(nota)
        return rezultat

    def get_toti_dupa_disciplina(self, id_disciplina):
        """
        Metoda read pentru toate notele din repository care au fost obtinute
        la o anumita disciplina
        :param id_disciplina: id ul disciplinei cautate
        :return: lista cu toate notele care au fost luate la disciplina data
        """
        rezultat = {}
        for nota in self.get_toti().values():
            if nota.get_id_disciplina() == id_disciplina:
                rezultat[nota.get_id_nota()] = nota
        return rezultat.values()


def test_stocare_nota():
    repository = RepositoryNoteStudent()
    assert repository.dimensiune() == 0

    student = Student(1, "Cezar")
    student = Student(2, "Ioana")
    student = Student(3, "Cristina")

    disciplina1 = Disciplina(1, "FP", "Czibula")
    disciplina2 = Disciplina(2, "Analiza", "Berinde")
    disciplina3 = Disciplina(3, "Algebra", "Modoi")
    nota = NotaStudent(1, 2, 1, 10)
    repository.stocare(nota)
    assert repository.dimensiune() == 1
    nota1 = repository.gaseste(1)
    assert nota == nota1

    nota = NotaStudent(1, 2, 2, 10)
    try:
        repository.stocare(nota)
        assert False
    except ExceptieIDDuplicat:
        assert True

test_stocare_nota()

def test_get_note():
    repository = RepositoryNoteStudent()

    student = Student(1, "Cezar")
    student = Student(2, "Ioana")
    student = Student(3, "Cristina")

    disciplina1 = Disciplina(1, "FP", "Czibula")
    disciplina2 = Disciplina(2, "Analiza", "Berinde")
    disciplina3 = Disciplina(3, "Algebra", "Modoi")

    nota = NotaStudent(1, 1, 1, 10)
    repository.stocare(nota)
    nota = NotaStudent(2, 1, 2, 10)
    repository.stocare(nota)
    nota = NotaStudent(3, 2, 1, 10)
    repository.stocare(nota)
    nota = NotaStudent(4, 2, 2, 10)
    repository.stocare(nota)
    nota = NotaStudent(5, 3, 2, 10)
    repository.stocare(nota)

    toate_notele = repository.get_toti()
    assert len(toate_notele) == 5
    toate_notele_lui_1 = repository.get_toti_dupa_student(1)
    assert len(toate_notele_lui_1) == 2
    toate_notele_la_2 = repository.get_toti_dupa_disciplina(2)
    assert len(toate_notele_la_2) == 3


test_get_note()