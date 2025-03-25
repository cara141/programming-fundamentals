from domeniu.validatori import ValidatorStudent
from domeniu.validatori import ValidatorDisciplina
from domeniu.validatori import ValidatorNota
from repository.memorie_repository import RepositoryStudent
from repository.memorie_repository import RepositoryDisciplina
from repository.memorie_repository import RepositoryNoteStudent
from domeniu.obiecte import Student
from domeniu.obiecte import Disciplina
from domeniu.obiecte import NotaStudent
from domeniu.validatori import ExceptieValidare
from domeniu.validatori import ExceptieCRUD
import random
import string
import copy

class ControllerStudent:
    """
    Clasa responsabila cu cazurile de utilizare a studentilor
    """
    def __init__(self, validator, repository):
        """
        Initializeaza controller ul,
        controller ul are nevoie de un validator si de un repository
        :param validator: ValidatorStudent
        :param repository: RepositoryStudent
        """
        self.__validator = validator
        self.__repository = repository

    def creeaza(self, id, nume):
        """
        Creaza, valideaza si stocheaza un student
        :param id: id student
        :param nume: nume student
        :return: Student
        arunca ValueError daca datele sunt invalide sau avem id duplicat
        """
        student = Student(id, nume)
        self.__validator.valideaza(student)
        self.__repository.stocare(student)
        return student

    def get_numar_studenti(self):
        """
        Returneaza numarul studentilor
        :return: int
        """
        return self.__repository.dimensiune()

    def sterge(self, id_student):
        """
        Sterge studentul cu id ul dat
        :param id_student: numar intreg id ul studentului de sters
        :return: Student, cel eliminat
        """
        return self.__repository.elimina(id_student)

    def cauta(self, criteriu):
        """
        Cauta studenti cu nume care contine criteriu
        :param criteriu: sir de caractere
        :return: lista studentilor, unde numele contine criteriu
        """
        toti = self.__repository.get_toti()
        if criteriu == "":
            return toti

        rezultat = []
        for student in toti.values():
            if criteriu in student.get_nume():
                rezultat.append(student)

        return rezultat

    def update(self, id, nume_nou):
        """
        update student cu id ul dat
        :param id: numar intreg
        :param nume_nou: sir de caractere
        :return: studentul vechi
        arunca ValueError daca studentul este invalid, sau daca nu exista
        studentul
        """
        student_nou = Student(id, nume_nou)
        self.__validator.valideaza(student_nou)
        student_vechi = self.__repository.gaseste(id)
        self.__repository.update(id, student_nou)
        return student_vechi

    def populeaza(self):
        """
        Functie care sa genereze un numar aleator de studenti cu nume
        aleatoare
        :return:
        """
        random.seed(1234)
        for id_student in range(1, random.randrange(50, 100, 1)):
            self.creeaza(id_student, "".join(random.choices(string.ascii_letters, k=10)))
    def sterge_toti(self):
        """
        Functie care elimina toti studentii
        :return:
        """
        self.__repository.elimina_tot()
def test_populeaza_studenti():
    """
    Functie de test pentru populare
    :return:
    """
    random.seed(1234)
    controller = ControllerStudent(ValidatorStudent(), RepositoryStudent())
    controller.populeaza()
    studenti1 = (controller.cauta(""))
    controller.sterge_toti()
    random.seed(1234)
    controller.populeaza()
    studenti2 = controller.cauta("")
    assert studenti2 == studenti1


test_populeaza_studenti()

def test_creare_student():
    """
    Functie de test pentru creare student
    Functionalitate 1 - adauga student
    Activitate 4 - creeaza controller student 
    """

    controller = ControllerStudent(ValidatorStudent(), RepositoryStudent())
    student = controller.creeaza(1, "Cezar")
    assert student.get_id() == 1
    assert student.get_nume() == "Cezar"
    assert controller.get_numar_studenti() == 1
    try:
        controller.creeaza(1, "")
        assert False
    except ExceptieValidare:
        assert True

    try:
        controller.creeaza(1, "Ioana")
        assert False
    except ExceptieCRUD:
        assert True

test_creare_student()

def test_stergere_student():
    """
    Functie de test pentru stergere student
    Functionalitate 2 - sterge student
    Activitate 2 - stergere student controller
    :return: 
    """
    controller = ControllerStudent(ValidatorStudent(), RepositoryStudent())
    student = controller.creeaza(1, "Cezar")
    try:
        controller.sterge(2)
        assert False
    except ValueError:
        assert True
    assert controller.get_numar_studenti() == 1

    student = controller.sterge(1)
    assert controller.get_numar_studenti() == 0
    assert student.get_id() == 1
    assert student.get_nume() == "Cezar"
    student = controller.creeaza(1, "Cezar")
    student = controller.creeaza(2, "Cezar")
    student = controller.creeaza(3, "Cezar")
    controller.sterge_toti()
    assert controller.get_numar_studenti() == 0
test_stergere_student()

def test_cautare_student():
    """
    Testare prima cautare
    Functionalitate 3 - listeaza toti studenti dupa un criteriu
    Activitate 2 - toti studenti care au un nume ce contine criteriu
    :return:
    """
    repository = RepositoryStudent()
    controller = ControllerStudent(ValidatorStudent(), repository)
    student1 = controller.creeaza(1, "Cezar")
    student2 = controller.creeaza(2, "Ioana")
    student3 = controller.creeaza(3, "Cristina")
    student4 = controller.creeaza(4, "Ion")
    student5 = controller.creeaza(5, "Pop")

    studenti = controller.cauta("Io")
    assert len(studenti) == 2
    assert student2 in studenti

    studenti = controller.cauta("")
    assert len(studenti) == 5

test_cautare_student()

def test_update_studenti():
    """
    Functie de test pentru update
    Functionalitate 4 - update informatii student
    Actiune 2 - update student controller
    :return:
    """
    controller = ControllerStudent(ValidatorStudent(), RepositoryStudent())
    student = controller.creeaza(1, "Cezar")
    student = controller.update(1, "Ioana")

    studenti = controller.cauta("Ioana")
    assert len(studenti) == 1
    assert student.get_nume() == "Cezar"

    try:
        student = controller.update(2, "Cristina")
        assert False
    except ValueError:
        assert True


test_update_studenti()

class ControllerDisciplina():
    """
    Clasa responsabila cu cazurile de utilizare pentru disciplina
    """

    def __init__(self, validator, repository):
        """
        Initializare controller, are nevoide de validator si de repository
        :param validator: ValidatorDisciplina
        :param repository: RepositoryDisciplina
        """
        self.__validator = validator
        self.__repository = repository

    def creeaza(self, id_disciplina, nume, profesor):
        """
        Creeaza, valideaza si stocheaza disciplina
        :param id: int
        :param nume: str
        :param profesor: str
        :return: Disciplina
        raise ValueError if invalid
        """
        disciplina_noua = Disciplina(id_disciplina, nume, profesor)
        self.__validator.valideaza(disciplina_noua)
        self.__repository.stocare(disciplina_noua)
        return disciplina_noua

    def get_numar_discipline(self):
        """
        :return: int, numarul de discipline
        """
        return self.__repository.dimensiune()

    def sterge(self, id):
        """
        Elimina disciplina cu id dat
        :param id: int
        :return: Disciplina socasa
        raise ValueError daca nu exista
        """
        return self.__repository.elimina(id)

    def sterge_tot(self):
        """
        Goleste lista de discipline
        :return: None
        """
        return self.__repository.elimina_tot()

    def cauta(self, criteriu):
        """
        Cauta disciplina dupa nume si criteriu
        :param criteriu: str
        :return: lista disciplinelor al caror nume contine criteriu
        """
        toti = self.__repository.get_toti()
        if criteriu == "":
            return toti

        rezultat = []
        for disciplina in toti.values():
            if criteriu in disciplina.get_nume():
                rezultat.append(disciplina)
        return rezultat

    def update(self, id, nume_nou, profesor_nou):
        """
        Update disciplina cu id dat
        :param id: int
        :param nume_nou: str
        :param profesor_nou: str
        :return: disciplina veche
        raise ValueError daca invalid
        """
        disciplina_noua = Disciplina(id, nume_nou, profesor_nou)
        self.__validator.valideaza(disciplina_noua)
        disciplina_veche = self.__repository.gaseste(id)
        self.__repository.update(id, disciplina_noua)
        return disciplina_veche

    def populeaza(self):
        random.seed(1234)
        for id_disciplina in range(1, random.randrange(50, 100, 1)):
            self.creeaza(id_disciplina, "".join(random.choices(string.ascii_letters, k=10)),
                         "".join(random.choices(string.ascii_letters, k=10)))

def test_creeaza_disciplina():
    """
    Testare functie creare disciplina
    Functionalitate 5 - adauga disciplina
    :return:
    """
    controller = ControllerDisciplina(ValidatorDisciplina(), RepositoryDisciplina())
    disciplina = controller.creeaza(1, "FP", "Czibula")
    assert disciplina.get_id() == 1
    assert disciplina.get_nume() == "FP"
    assert disciplina.get_profesor() == "Czibula"
    assert controller.get_numar_discipline() == 1


test_creeaza_disciplina()
def test_sterge_disciplina():
    controller = ControllerDisciplina(ValidatorDisciplina(), RepositoryDisciplina())
    disciplina = controller.creeaza(1, "FP", "Czibula")

    disciplina = controller.sterge(1)
    assert controller.get_numar_discipline() == 0
    assert disciplina.get_id() == 1
    assert disciplina.get_nume() == "FP"

test_sterge_disciplina()

def test_cauta_disciplina():
    controller = ControllerDisciplina(ValidatorDisciplina(), RepositoryDisciplina())
    disciplina1 = controller.creeaza(1, "FP", "Czibula")
    disciplina2 = controller.creeaza(2, "LC", "Pop")
    disciplina3 = controller.creeaza(3, "Analiza", "Berinde")
    disciplina4 = controller.creeaza(4, "Analiza1", "Berinde")

    discipline = controller.cauta("Analiza")
    assert len(discipline) == 2
    assert disciplina4 in discipline

    discipline = controller.cauta("")
    assert len(discipline) == 4


test_cauta_disciplina()
def test_update_disciplina():
    controller = ControllerDisciplina(ValidatorDisciplina(), RepositoryDisciplina())
    disciplina = controller.creeaza(1, "FP", "Czibula")
    disciplina = controller.update(1, "Analiza", "Berinde")

    discipline = controller.cauta(("Analiza"))
    assert len(discipline) == 1
    assert disciplina.get_nume() == "FP"

test_update_disciplina()
def test_populeaza_disciplina():
    random.seed(1234)
    controller = ControllerDisciplina(ValidatorDisciplina(), RepositoryDisciplina())
    controller.populeaza()
    discipline1 = (controller.cauta(""))
    controller.sterge_tot()
    random.seed(1234)
    controller.populeaza()
    discipline2 = controller.cauta("")
    assert discipline2 == discipline1

test_populeaza_disciplina()

class StudentNuExistaExceptie(ExceptieCRUD):
    def __init__(self):
        pass

class DisciplinaNuExistaExceptie(ExceptieCRUD):
    def __init__(self):
        pass

class ControllerNote:
    def __init__(self, repository_note, validator_note, repository_student, repository_discipline):
        self.__repo_note = repository_note
        self.__repo_studenti = repository_student
        self.__repo_discipline = repository_discipline
        self.__val_note = validator_note

    def atribuie(self, id_nota, id_student, id_disciplina, scor):
        """
        Atribuie nota
        :param id_nota: int
        :param id_student: int
        :param id_disciplina: int
        :param scor: float
        :return: Grade
        """

        student = self.__repo_studenti.gaseste(id_student)
        if student == None:
            raise StudentNuExistaExceptie()
        nota = NotaStudent(id_nota, id_student, id_disciplina, scor)
        self.__val_note.valideaza(nota)
        self.__repo_note.stocare(nota)
        return nota

    def statistici_disciplina(self, id_disciplina):
        """
        Lista studenti dupa disciplina
        :param id_disciplina: int
        :return: list (Student, Grade)
        """
        disciplina = self.__repo_discipline.gaseste(id_disciplina)
        if disciplina is None:
            raise DisciplinaNuExistaExceptie()

        note_disciplina = [(self.__repo_studenti.gaseste(nota.get_id_student()), nota) for nota in
                           self.__repo_note.get_toti().values() if nota.get_id_disciplina() == id_disciplina]


        note_disciplina.sort(key=lambda x: (x[0].get_nume(), x[1].get_scor()))

        return note_disciplina

    def top_20_students(self):
        """
        Top 20% in functie de toate notele
        :return: Lista de tupluri (Student, average_grade)
        """
        toti = self.__repo_studenti.get_toti().values()


        note_medii = []
        for student in toti:
            note = self.__repo_note.get_toti_dupa_student(student.get_id())
            if note:
                avg_grade = sum(grade.get_scor() for grade in note) / len(note)
                note_medii.append((student, avg_grade))


        studenti_sortati = sorted(note_medii, key=lambda x: x[1], reverse=True)


        top_20_numar = int(0.2 * len(studenti_sortati))

        return studenti_sortati[:top_20_numar]

    def top_20_discipline(self):
        """
        Top 20% discipline ordonate dupa numarul studentilor care au nota la materie
        :return:
        """

        toate = self.__repo_discipline.get_toti().values()

        note_medii = []
        for disciplina in toate:
            note = self.__repo_note.get_toti_dupa_disciplina(disciplina.get_id())
            if note:
                avg_grade = sum(grade.get_scor() for grade in note) / len(note)
                note_medii.append((disciplina, avg_grade))

        discipline_sortate = sorted(note_medii, key=lambda x: x[1], reverse=True)

        top_20_numar = int(0.2 * len(discipline_sortate))

        return discipline_sortate[:top_20_numar]

def test_top_20_discipline():
    repo_studenti = RepositoryStudent()
    repo_discipline = RepositoryDisciplina()
    val_studenti = ValidatorStudent()
    val_disciplina = ValidatorDisciplina()
    controller_studenti = ControllerStudent(val_studenti, repo_studenti)
    controller_discipline = ControllerDisciplina(val_disciplina, repo_discipline)
    controller_note = ControllerNote(RepositoryNoteStudent(), ValidatorNota(), repo_studenti, repo_discipline)

    student1 = controller_studenti.creeaza(1, "Cezar")
    student2 = controller_studenti.creeaza(2, "Ioana")
    student3 = controller_studenti.creeaza(3, "Cristina")


    disciplina1 = controller_discipline.creeaza(1, "Analiza", "Berinde")
    disciplina2 = controller_discipline.creeaza(2, "Algebra", "Modoi")
    disciplina3 = controller_discipline.creeaza(3, "FP", "Czibula")
    disciplina4 = controller_discipline.creeaza(4, "LC", "Pop")
    disciplina5 = controller_discipline.creeaza(5, "ASC", "Vancea")
    disciplina6 = controller_discipline.creeaza(6, "Analiza2", "Berinde")

    controller_note.atribuie(1, 1, 1, 9.5)
    controller_note.atribuie(2, 2, 2, 9.5)
    controller_note.atribuie(3, 3, 3, 7.5)
    controller_note.atribuie(4, 3, 4, 9.0)
    controller_note.atribuie(5, 3, 5, 8.5)

    top_discipline = controller_note.top_20_discipline()

    assert len(top_discipline) == 1
    assert top_discipline[0] == (disciplina1, 9.5)

test_top_20_discipline()

def test_atribuie_nota():
    repo_studenti = RepositoryStudent()
    repo_discipline = RepositoryDisciplina()
    val_studenti = ValidatorStudent()
    val_disciplina = ValidatorDisciplina()
    controller_studenti = ControllerStudent(val_studenti, repo_studenti)
    controller_discipline = ControllerDisciplina(val_disciplina, repo_discipline)
    controller = ControllerNote(RepositoryNoteStudent(), ValidatorNota(), repo_studenti, repo_discipline)

    student = controller_studenti.creeaza(1, "Cezar")
    disciplina = controller_discipline.creeaza(1, "Analiza", "Berinde")
    nota = controller.atribuie(1, 1, 1, 10)



test_atribuie_nota()


def test_statistici_disciplina():
    repo_studenti = RepositoryStudent()
    repo_discipline = RepositoryDisciplina()
    val_studenti = ValidatorStudent()
    val_disciplina = ValidatorDisciplina()
    repo_note = RepositoryNoteStudent()
    val_note = ValidatorNota()

    controller_studenti = ControllerStudent(val_studenti, repo_studenti)
    controller_discipline = ControllerDisciplina(val_disciplina, repo_discipline)
    controller_note = ControllerNote(repo_note, val_note, repo_studenti, repo_discipline)

    student1 = controller_studenti.creeaza(1, "Ana")
    student2 = controller_studenti.creeaza(2, "Bogdan")
    student3 = controller_studenti.creeaza(3, "Cezar")

    disciplina = controller_discipline.creeaza(1, "Matematica", "Prof. Popescu")

    nota1 = controller_note.atribuie(1, 1, 1, 9.5)
    nota2 = controller_note.atribuie(2, 2, 1, 8.0)
    nota3 = controller_note.atribuie(3, 3, 1, 9.0)

    note_disciplina = controller_note.statistici_disciplina(1)

    assert len(note_disciplina) == 3
    assert note_disciplina[0] == (student1, nota1)
    assert note_disciplina[1] == (student2, nota2)
    assert note_disciplina[2] == (student3, nota3)


def test_top_20_percent():
    repo_studenti = RepositoryStudent()
    repo_discipline = RepositoryDisciplina()
    val_studenti = ValidatorStudent()
    val_disciplina = ValidatorDisciplina()
    controller_studenti = ControllerStudent(val_studenti, repo_studenti)
    controller_discipline = ControllerDisciplina(val_disciplina, repo_discipline)
    controller_note = ControllerNote(RepositoryNoteStudent(), ValidatorNota(), repo_studenti, repo_discipline)

    student1 = controller_studenti.creeaza(1, "Cezar")
    student2 = controller_studenti.creeaza(2, "Ioana")
    student3 = controller_studenti.creeaza(3, "Cristina")
    student4 = controller_studenti.creeaza(4, "Ion")
    student5 = controller_studenti.creeaza(5, "Pop")

    disciplina1 = controller_discipline.creeaza(1, "Analiza", "Berinde")

    controller_note.atribuie(1, 1, 1, 9.5)
    controller_note.atribuie(2, 2, 1, 8.0)
    controller_note.atribuie(3, 3, 1, 7.5)
    controller_note.atribuie(4, 4, 1, 9.0)
    controller_note.atribuie(5, 5, 1, 8.5)

    top_students = controller_note.top_20_students()

    assert len(top_students) == 1
    assert top_students[0] == (student1, 9.5)

test_statistici_disciplina()
test_top_20_percent()