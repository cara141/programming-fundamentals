from controllers.controllers import ControllerStudent, ControllerDisciplina, ControllerNote
from domeniu.obiecte import Student, Disciplina
from domeniu.validatori import ValidatorStudent, ValidatorDisciplina, ValidatorNota
from repository.repository import RepositoryStudent, RepositoryDisciplina, RepositoryNoteStudent

class ConsoleUI:
    def __init__(self):
        self.validator_student = ValidatorStudent()
        self.validator_disciplina = ValidatorDisciplina()
        self.repository_student = RepositoryStudent()
        self.repository_disciplina = RepositoryDisciplina()
        self.repository_note = RepositoryNoteStudent()
        self.validator_note = ValidatorNota()
        self.controller_studenti = ControllerStudent(self.validator_student, self.repository_student )
        self.controller_discipline = ControllerDisciplina(self.validator_disciplina, self.repository_disciplina)
        self.controller_note = ControllerNote(self.repository_note, self.validator_note , self.repository_student, self.repository_disciplina)
        self.controller_studenti.populeaza()
        self.controller_discipline.populeaza()

    def run(self):

        self.controller_note.atribuie(1, 8, 33, 10.0)
        self.controller_note.atribuie(2, 9, 33, 9.0)
        self.controller_note.atribuie(3, 10, 11, 8.5)
        self.controller_note.atribuie(4, 11, 12, 7.0)
        self.controller_note.atribuie(5, 12, 13, 2.5)
        self.controller_note.atribuie(6, 12, 14, 3.0)

        while True:
            print("\n1. Adaugare student")
            print("2. Stergere student")
            print("3. Modificare student")
            print("4. Cautare student")
            print("5. Adaugare disciplina")
            print("6. Stergere disciplina")
            print("7. Modificare disciplina")
            print("8. Cautare disciplina")
            print("9. Atribuire nota")
            print("10. Statistici")
            print("0. Iesire")

            option = input("Selectati optiunea: ")

            if option == "1":
                self.adauga_student()
            elif option == "2":
                self.sterge_student()
            elif option == "3":
                self.modifica_student()
            elif option == "4":
                self.cauta_student()
            elif option == "5":
                self.adauga_disciplina()
            elif option == "6":
                self.sterge_disciplina()
            elif option == "7":
                self.modifica_disciplina()
            elif option == "8":
                self.cauta_disciplina()
            elif option == "9":
                self.atribuie_nota()
            elif option == "10":
                self.afiseaza_statistici()
            elif option == "0":
                break
            else:
                print("Optiune invalida! Va rugam sa introduceti o optiune valida.")

    def adauga_student(self):
        id_student = int(input("Introduceti ID-ul studentului: "))
        nume_student = input("Introduceti numele studentului: ")
        self.controller_studenti.creeaza(id_student, nume_student)
        print("Student adaugat cu succes!")

    def sterge_student(self):
        id_student = int(input("Introduceti ID-ul studentului de sters: "))
        try:
            student = self.controller_studenti.sterge(id_student)
            print(f"Studentul {student.get_nume()} a fost sters cu succes!")
        except ValueError as ve:
            print(ve)

    def modifica_student(self):
        id_student = int(input("Introduceti ID-ul studentului de modificat: "))
        nume_nou = input("Introduceti noul nume al studentului: ")
        try:
            student_vechi = self.controller_studenti.update(id_student, nume_nou)
            print(f"Studentul {student_vechi.get_nume()} a fost modificat cu succes!")
        except ValueError as ve:
            print(ve)

    def cauta_student(self):
        criteriu = input("Introduceti criteriul de cautare: ")
        studenti_gasiti = self.controller_studenti.cauta(criteriu)
        if not studenti_gasiti:
            print("Nu s-au gasit studenti conform criteriului.")
        else:
            print("Studenti gasiti:")
            if criteriu == "":
                for student in studenti_gasiti.values():
                    print(student.__str__())
            else:
                for student in studenti_gasiti:
                    print(student.__str__())
    def adauga_disciplina(self):
        id_disciplina = int(input("Introduceti ID-ul disciplinei: "))
        nume_disciplina = input("Introduceti numele disciplinei: ")
        profesor_disciplina = input("Introduceti numele profesorului: ")
        self.controller_discipline.creeaza(id_disciplina, nume_disciplina, profesor_disciplina)
        print("Disciplina adaugata cu succes!")

    def sterge_disciplina(self):
        id_disciplina = int(input("Introduceti ID-ul disciplinei de sters: "))
        try:
            disciplina = self.controller_discipline.sterge(id_disciplina)
            print(f"Disciplina {disciplina.get_nume()} a fost stearsa cu succes!")
        except ValueError as ve:
            print(ve)

    def modifica_disciplina(self):
        id_disciplina = int(input("Introduceti ID-ul disciplinei de modificat: "))
        nume_nou = input("Introduceti noul nume al disciplinei: ")
        profesor_nou = input("Introduceti noul profesor al disciplinei: ")
        try:
            disciplina_veche = self.controller_discipline.update(id_disciplina, nume_nou, profesor_nou)
            print(f"Disciplina {disciplina_veche.get_nume()} a fost modificata cu succes!")
        except ValueError as ve:
            print(ve)

    def cauta_disciplina(self):
        criteriu = input("Introduceti criteriul de cautare: ")
        discipline_gasite = self.controller_discipline.cauta(criteriu)
        if not discipline_gasite:
            print("Nu s-au gasit discipline conform criteriului.")
        else:
            print("Discipline gasite:")
            if criteriu == "":
                for disciplina in discipline_gasite.values():
                    print(disciplina.__str__())
            else:
                for disciplina in discipline_gasite:
                    print(disciplina.__str__())
    def atribuie_nota(self):
        id_nota = int(input("Introduceti ID-ul notei: "))
        id_student = int(input("Introduceti ID-ul studentului: "))
        id_disciplina = int(input("Introduceti ID-ul disciplinei: "))
        scor = float(input("Introduceti scorul notei: "))
        try:
            nota = self.controller_note.atribuie(id_nota, id_student, id_disciplina, scor)
            print(f"Nota {nota.get_scor()} atribuita studentului {id_student} la disciplina {id_disciplina} cu succes!")
        except ValueError as ve:
            print(ve)

    def lista_studenti_disciplina_ordonat(self):
        id_disciplina = int(input("Introduceti ID-ul disciplinei pentru care doriti statistici: "))
        studenti_note = self.controller_note.statistici_disciplina(id_disciplina)

        if not studenti_note:
            print("Nu exista note pentru disciplina data.")
        else:
            print("Lista de studenti si notele lor, ordonat alfabetic dupa nume, dupa nota:")
            for student, nota in studenti_note:
                print(f"{student.get_nume()} - {nota.get_scor()}")

    def primii_20_studenti(self):
        studenti_20_procent = self.controller_note.top_20_students()

        print("Primi 20% din studenti ordonati dupa media notelor la toate disciplinele:")
        for student in studenti_20_procent:
            print(student[0])

    def primele_20_discipline(self):
        primele_20_discipline = self.controller_note.top_20_discipline()

        print("Primele 20% din discipline ordonate dupa media notelor tuturor studentilor:")
        for disciplina in primele_20_discipline:
            print(disciplina[0])

    def afiseaza_statistici(self):
        print("Statistici:")
        print("1. Lista de studenti si notele lor la o disciplina data, ordonat: alfabetic dupa nume, dupa nota.")
        print("2. Primi 20% din studenti ordonati dupa media notelor la toate disciplinele.")
        print("3. Primele 20% din discipline ordonate dupa numarul notelor la toate disciplinele.")
        optiune = input("Selectati optiunea pentru statistici: ")

        if optiune == "1":
            self.lista_studenti_disciplina_ordonat()
        elif optiune == "2":
            self.primii_20_studenti()
        elif optiune == "3":
            self.primele_20_discipline()
        else:
            print("Nu exista optiunea!")



if __name__ == "__main__":
    ui = ConsoleUI()
    ui.run()
