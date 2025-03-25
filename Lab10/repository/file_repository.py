from repository.memorie_repository import RepositoryStudent
from repository.memorie_repository import RepositoryDisciplina
from repository.memorie_repository import RepositoryNoteStudent
from repository.memorie_repository import ExceptieRepository
from domeniu.obiecte import Student
from domeniu.obiecte import Disciplina
from domeniu.obiecte import NotaStudent

class RepositoryStudentFisier(RepositoryStudent):
    """
    Stocheaza/Preia studenti din fisier
    """
    def __init__(self, fisier):
        """
        Initializarea repository
        :param fisier: string, calea catre fisierul unde sunt tinuti
        studentii
        """
        RepositoryStudent.__init__(self)
        self.__nume_fisier = fisier

        self.__incarca_din_fisier()

    def __incarca_din_fisier(self):
        """
        Incarca studenti din fisier
        :return: CorruptedFileException daca exista eroare la citirea din
        fisier
        """
        try:
            fisier = open(self.__nume_fisier, "r")
        except IOError:
            return
        linie = fisier.readline().strip()
        while linie != "":
            atribute = linie.split(",")
            student = Student(int(atribute[0]), atribute[1])
            RepositoryStudent.stocare(self, student)
            linie = fisier.readline().strip()
        fisier.close()

    def stocare(self, student):
        """
        Stocheaza studentul la file.Overwrite store
        :param student: studentul
        :return: None
        Post: studentul este in fisier
        :raise: ExceptieIDDuplicat pentru id duplicat
        """
        RepositoryStudent.stocare(self, student)
        self.__stocare_in_fisier()

    def update(self, id, student):
        """
        Update student in repository
        :param id: int, id ul studentului de modificat
        :param student: student, noul student
        :return: ValueError daca nu exista student cu id dat
        """
        RepositoryStudent.update(self, id, student)
        self.__stocare_in_fisier()

    def elimina(self, id_student):
        """
        Elimina un student din repository
        :param id_student: id ul studentului de eliminat
        :return: studentul eliminat
        :post: repo nu continte studentul cu id ul dat
        :raise: ValueError daca nu exista student cu id dat
        """
        RepositoryStudent.elimina(self, id_student)
        self.__stocare_in_fisier()

    def __stocare_in_fisier(self):
        """
        Stocare tuturor studentilor in fisierul specific repoului
        :return: None.
        :raise: CorruptedFileException daca nu se poate realiza op
        """
        fisier = open(self.__nume_fisier, "w")
        studenti = RepositoryStudent.get_toti(self).values()
        for student in studenti:
            string_student = str(student.get_id())+','+student.get_nume()
            string_student = string_student + '\n'
            fisier.write(string_student)
        fisier.close()

    def elimina_tot(self):
        """
        Goleste repo
        :return: None
        :post: Repo gol
        """
        RepositoryStudent.elimina_tot(self)
        self.__stocare_in_fisier()

def test_repository_student_fisier():
    nume_fisier = "teststudent.txt"
    repository = RepositoryStudentFisier(nume_fisier)
    repository.elimina_tot()

    assert repository.dimensiune() == 0
    student = Student(1, "Cezar")
    repository.stocare(student)
    assert repository.dimensiune() == 1
    assert repository.gaseste(1).get_id() == 1
    assert repository.gaseste(1).get_nume() == "Cezar"

    repository1 = RepositoryStudentFisier(nume_fisier)
    assert repository1.dimensiune() == 1
    assert repository1.gaseste(1) == student
    try:
        repository1.stocare(student)
        assert False
    except ExceptieRepository:
        assert True

    student.set_id(2)
    repository1.stocare(student)
    assert repository1.gaseste(2) == student

test_repository_student_fisier()

class RepositoryDisciplinaFisier(RepositoryDisciplina):
    """
    Stocheaza / Preia studentii din fisiere
    """
    def __init__(self, nume_fisier):
        """
        Initializare repository fisier
        :param nume_fisier: numele fisierului din care preia datele despre
        discipline
        """
        RepositoryDisciplina.__init__(self)
        self.__nume_fisier = nume_fisier
        self.__incarca_din_fisier()

    def __incarca_din_fisier(self):
        """
        Preia din fisier toate datele despre disciplina
        :raise: CorruptedFileException daca nu exista
        """
        try:
            fisier = open(self.__nume_fisier, "r")
        except IOError:
            return
        linie = fisier.readline().strip()
        while linie != "":
            atribute = linie.split(",")
            disciplina = Disciplina(int(atribute[0]), atribute[1], atribute[2])
            RepositoryDisciplina.stocare(self, disciplina)
            linie = fisier.readline().strip()
        fisier.close()

    def __stocare_in_fisier(self):
        """
        Stocheaza toate disciplinele in fisier
        :raise: CorruptedFileException daca nu exista
        """
        fisier = open(self.__nume_fisier, "w")
        discipline = RepositoryDisciplina.get_toti(self).values()
        for disciplina in discipline:
            string_disciplina = str(disciplina.get_id()) + ',' + disciplina.get_nume() + ',' + disciplina.get_profesor()
            string_disciplina = string_disciplina + '\n'
            fisier.write(string_disciplina)
        fisier.close()

    def stocare(self, disciplina):
        """
        Stocheaza disciplina in repo
        :param disciplina: disciplina de adaugat in repo
        :return: None
        :raise: ExceptieIDDuplicat pentru id duplicat
        """
        RepositoryDisciplina.stocare(self, disciplina)
        self.__stocare_in_fisier()

    def elimina(self, id_disciplina):
        """
        Elimina disciplina cu id ul dat din repo
        :param id_disciplina: id ul discplinei de adaugat
        :return: disciplian elim
        raise ExceptieRepository daca nu exista
        """
        RepositoryDisciplina.elimina(self, id_disciplina)
        self.__stocare_in_fisier()

    def elimina_tot(self):
        """
        Elimina toti studentii din repository
        :return:
        """
        RepositoryDisciplina.elimina_tot(self)
        self.__stocare_in_fisier()

    def update(self, id_disciplina, disciplina_noua):
        """
        Modifica studentul din repository cu id ul nou
        :param id_disciplina:
        :param disciplina_noua:
        :return:
        """
        RepositoryDisciplina.update(self, id_disciplina, disciplina_noua)
        self.__stocare_in_fisier()




def test_repository_disciplina_fisier():
    nume_fisier = "testdisciplina.txt"
    repository = RepositoryDisciplinaFisier(nume_fisier)
    repository.elimina_tot()
    assert repository.dimensiune() == 0

    disciplina = Disciplina(1, "FP", "Czibula")
    repository.stocare(disciplina)
    assert repository.dimensiune() == 1
    assert repository.gaseste(1) == disciplina

    repository1 = RepositoryDisciplinaFisier(nume_fisier)
    assert repository1.dimensiune() == 1
    assert repository1.gaseste(1) == disciplina
    try:
        repository1.stocare(disciplina)
        assert False
    except ExceptieRepository:
        assert True

test_repository_disciplina_fisier()

class RepositroyNoteStudentFisier(RepositoryNoteStudent):
    """
    Adauga/Citeste/Elimina/Modifica date din fisier pt note
    """
    def __init__(self, nume_fisier):
        """
        Initializare repository pt fisierul specificat
        :param nume_fisier:  numele fisierului ce vq fi deschis
        """
        RepositoryNoteStudent.__init__(self)
        self.__nume_fisier = nume_fisier
        self.__incarca_din_fisier()

    def __incarca_din_fisier(self):
       try:
           fisier = open(self.__nume_fisier, "r")
       except IOError:
           return
       linie = fisier.readline().strip()
       while linie != "":
           atribute = linie.split(",")
           nota = NotaStudent(int(atribute[0]), int(atribute[1]), int(atribute[2]), float(atribute[3]))
           RepositoryNoteStudent.stocare(self,nota)
           linie = fisier.readline().strip()
       fisier.close()

    def __stocare_in_fisier(self):
        fisier = open(self.__nume_fisier, 'w')
        note = RepositoryNoteStudent.get_toti(self).values()
        for nota in note:
            string_nota = str(nota.get_id_nota())+','+str(nota.get_id_student())
            string_nota = string_nota+','+str(nota.get_id_disciplina())+','
            string_nota = string_nota+str(nota.get_scor())+'\n'
            fisier.write(string_nota)
        fisier.close()


    def stocare(self, nota):
        RepositoryNoteStudent.stocare(self, nota)
        self.__stocare_in_fisier()

    def elimina_tot(self):
        RepositoryNoteStudent.elimina_tot(self)
        self.__stocare_in_fisier()

def test_repository_note_student_fisier():
    nume_fisier = "testnote.txt"
    repository = RepositroyNoteStudentFisier(nume_fisier)
    repository.elimina_tot()
    assert repository.dimensiune() == 0
    nota = NotaStudent(1, 1, 1, 10)
    repository.stocare(nota)
    assert repository.dimensiune() == 1
    assert repository.gaseste(1) == nota
    try:
        repository.stocare(nota)
        assert False
    except ExceptieRepository:
        assert True

    repository1 = RepositroyNoteStudentFisier(nume_fisier)
    assert repository1.dimensiune() == 1
    assert repository1.gaseste(1) == nota

test_repository_note_student_fisier()