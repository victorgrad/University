from Controller.control import *


class Consola:
    """
    Consola
    """
    def __init__(self, service):
        self.__initCommands()
        self.service = service
        self.meniu = "\nComenzi posibile:\nadaugare ----------> Adauga studenti, discipline sau note in catalog\n" \
                                          "stergere ----------> Sterge studenti, discipline sau note din catalog\n" \
                                          "modificare --------> Modifica stundenti sau discipline din catalog\n" \
                                          "cautare  ----------> Cauta studenti sau discipline din catalog\n"\
                                          "generare ----------> Genereaza studenti sau discipline in catalog\n"\
                                          "statistici --------> Afiseaza statistici despre studentii din catalog\n"\
                                          "afisare  ----------> Afiseaza studentii,disciplinele sau notele din catalog\n"\
                                          "exit     ----------> Iesire din program\n"

    def __initCommands(self):
        """
        Initializarea comenzilor
        :return:
        """
        self.dict = {"adaugare": {"student": self.__s_adaugare,
                                  "disciplina": self.__d_adaugare,
                                  "nota": self.__n_adaugare},
                     "stergere": {"student": self.__s_stergere,
                                  "disciplina": self.__d_stergere,
                                  "nota": self.__n_stergere},
                     "modificare": {"student": self.__s_modificare,
                                    "disciplina": self.__d_modificare},
                     "afisare": {"studenti": self.__s_afisare,
                                 "note": self.__n_afisare,
                                 "discipline": self.__d_afisare},
                     "cautare": {"student": self.__s_cautare,
                                 "disciplina": self.__d_cautare},
                     "generare": {"student": self.__s_generare,
                                  "disciplina": self.__d_generare},
                     "statistici": {"1": self.__st_lista,
                                    "2": self.__st_top,
                                    "3": self.__st_top_dis},
                     "exit": "ceva random"
                     }

    def __st_top_dis(self):
        """
        Afisarea a top 20% listei de studenti ordonat dupa media lor la o disciplina data
        :return:
        """
        intrare = input("Introduceti id-ul disciplinei la care doriti sa generati statistica: ")
        try:
            lista = self.service.afiseaza_top_dis(intrare)
            for i in range(0, int(len(lista) / 5)):
                print(lista[i].get_nume(), lista[i].get_prenume(), "media:", lista[i].discipline[intrare].get_media())
        except Eroare as er:
            print(er)

    def __st_lista(self):
        """
        Afisarea listei de studenti ordonat dupa nume sau nota la o anumita disciplina
        :return:
        """
        intrare = input("Introduceti id-ul disciplinei la care doriti sa creati o statistica: ")

        student_temporar = Student(999999999, "test", "bot")
        self.service.Repository.c1.store(student_temporar)
        if intrare not in self.service.Repository.c1.ctl[999999999].discipline:
            self.service.Repository.c1.delete(999999999)
            print("Disciplina inexistenta")
        else:
            self.service.Repository.c1.delete(999999999)
            print("Dupa ce doriti sortarea listei?\nOptiuni posibile: nume, nota")
            dpc = input()
            lista = self.service.afiseaza_ordonat(intrare, dpc)
            for i in range(0, len(lista)):
                print(lista[i].nume, "notele:", lista[i].note)


    def __st_top(self):
        """
        Afisarea a top 20% listei de studenti ordonat dupa media lor generala
        :return:
        """
        lista = self.service.afiseaza_top()
        for i in range(0, int(len(lista)/5)):
            print(lista[i].nume, "media:", lista[i].media)


    def __s_afisare(self):
        """
        Afisarea catalogului(a elevilor)
        :return:
        """
        self.service.afiseaza_studenti()

    def __n_adaugare(self):
        """
        Aduga note in catalog
        :return:
        """
        print("Introduceti id-ul studentului, id-ul disciplinei si nota separate printr-un spatiu")
        intrare = input()
        intrare = intrare.split(' ')
        try:
            self.service.Repository.v.validare_nota(int(intrare[2]))
            self.service.adauga_nota(int(intrare[0]), intrare[1], int(intrare[2]))
            student_temporar = Student(999999999, "test", "bot")
            self.service.Repository.c1.store(student_temporar)
            print("A fost adaugata nota", intrare[2], "studentului/ei", self.service.Repository.c1.ctl[int(intrare[0])].get_nume(), self.service.Repository.c1.ctl[int(intrare[0])].get_prenume(),
                  "la disciplina", self.service.Repository.c1.ctl[999999999].discipline[intrare[1]].get_nume())
            self.service.Repository.c1.delete(999999999)
        except IndexError as ie:
            print("Nu ati introdus datele corespunzatoare")
        except Eroare as ex:
            print(ex)
        except:
            print("Nu ati introdus datele corespunzatoare!")



    def __n_stergere(self):
        """
        Sterge note in catalog
        :return:
        """
        print("Introduceti id-ul studentului, id-ul disciplinei si nota separate printr-un spatiu")
        intrare = input()
        intrare = intrare.split(' ')
        try:
            self.service.Repository.v.validare_nota(int(intrare[2]))
            self.service.sterge_nota(int(intrare[0]), intrare[1], int(intrare[2]))
            student_temporar = Student(999999999, "test", "bot")
            self.service.Repository.c1.store(student_temporar)
            print("A fost stearsa nota", intrare[2], "studentului/ei",
                  self.service.Repository.c1.ctl[int(intrare[0])].get_nume(),
                  self.service.Repository.c1.ctl[int(intrare[0])].get_prenume(),
                  "de la disciplina", self.service.Repository.c1.ctl[999999999].discipline[intrare[1]].get_nume())
            self.service.Repository.c1.delete(999999999)
        except IndexError as ie:
            print("Nu ati introdus datele corespunzatoare")
        except Eroare as ex:
            print(ex)
        except:
            print("Nu ati introdus datele corespunzatoare!")

    def __n_afisare(self):
        """
        Afiseaza notele din catalog
        :return:
        """
        print("Introduceti id-ul studentului ale carui note doriti sa le vedeti")
        intrare = input()
        try:
            self.service.afiseaza_note(int(intrare))
        except Eroare as ex:
            print(ex)

    def __d_afisare(self):
        """
        Afisarea disciplinelor
        :return:
        """
        self.service.afiseaza_discipline()

    def __d_stergere(self):
        """
        Functia __d_stergere sterge disciplina din catalog
        :return:
        """
        intrare = input(
            "Introduceti indexul disciplinei pe care doriti sa o stergeti ")
        self.service.sterge_disciplina(intrare)

    def __d_modificare(self):
        """
        Functia __d_modificare modifica date despre discipline
        :return:
        """
        print("Introduceti id-ul disciplinei pe care doriti sa o modificati")
        try:
            idi = input()
            student_temporar = Student(999999999, "test", "bot")
            self.service.Repository.c1.store(student_temporar)
            if idi in self.service.Repository.c1.ctl[999999999].discipline:
                print("Ce doriti sa modificati?\nOptiuni posibile: nume, profesor")
                opt = input()
                if opt == "nume":
                    print("Introduceti noul nume al disciplinei")
                    newn = input()
                    self.service.Repository.modificare_d_nume(idi, newn)
                elif opt == "profesor":
                    print("Introduceti noul profesor al disciplinei")
                    newn = input()
                    self.service.Repository.modificare_d_profesor(idi, newn)
            else:
                print("Id inexistent")
            self.service.Repository.c1.delete(999999999)

        except ValueError:
            print("Nu ati introdus datele corespunzatoare")

    def __d_adaugare(self):
        """
        Functia __d_adaugare adauga disciplina in catalog
        :return:
        """
        print("Introduceti datele disciplinei separate printr-o virgula sub forma id(1234)sau(mate), nume(Matematica), profesor(Ion Pop)\nATENTIE: ID-UL NU VA PUTEA FI SCHIMBAT ULTERIOR")
        intrare = input()
        intrare = intrare.split(', ')
        try:
            profesor = intrare[2]
            self.service.adauga_disciplina(intrare[0], intrare[1], profesor)
        except IndexError:
            print("Nu ati introdus datele corespunzatoare")
        except ValueError:
            print("Nu ati introdus un index valid")

    def __s_stergere(self):
        """
        Functia __s_stergere sterge studenti din catalog
        :return:
        """
        print("Introduceti id-ul studentului pe care doriti sa il stergeti")
        try:
            intrare = int(input())
            self.service.sterge_student(intrare)
        except IndexError:
            print("Nu ati introdus un index valid")
        except ValueError:
            print("Nu ati introdus datele corespunzatoare")

    def __s_modificare(self):
        """
        Functia __s_modificare modifica date despre student
        :return:
        """
        print("Introduceti id-ul studentului pe care doriti sa il modificati")
        try:
            idi = int(input())
            if idi in self.service.Repository.c1.ctl:
                print("Ce doriti sa modificati?\nOptiuni posibile: nume, prenume")
                opt = input()
                if opt == "nume":
                    print("Introduceti noul nume al studentului")
                    newn = input()
                    self.service.Repository.modificare_s_nume(idi, newn)
                elif opt == "prenume":
                    print("Introduceti noul prenume al studentului")
                    newn = input()
                    self.service.Repository.modificare_s_prenume(idi, newn)
            else:
                print("Id inexistent")

        except ValueError:
            print("Nu ati introdus datele corespunzatoare")

    def __s_adaugare(self):
        """
        Functia __s_adaugare adauga studenti in catalog
        :return:
        """
        print("Introduceti datele studentului separate printr-un spatiu sub forma id(1234) nume(Pop) prenume(Ion)\nATENTIE: ID-UL NU VA PUTEA FI SCHIMBAT ULTERIOR")
        intrare = input()
        intrare = intrare.split(' ')
        try:
            self.service.adauga_student(int(intrare[0]), intrare[1], intrare[2])
        except IndexError:
            print("Nu ati introdus un index valid")
        except ValueError:
            print("Nu ati introdus datele corespunzatoare")

    def __s_cautare(self):
        """
        Functia __s_cautare este componenta UI care primeste date despre student (id sau nume) si afiseaza date despre el
        :return:
        """
        intrare = input(
            "Introduceti indexul sau numele studentului pe care doriti sa il cautati: ")
        try:
            print(self.service.cauta_student(intrare))
        except Eroare as ex:
            print(ex)

    def __d_cautare(self):
        """
        Functia __d_cautare este componenta UI care primeste date despre disciplina (id, nume, sau nume profesor) si afiseaza date despre ea
        :return:
        """
        intrare = input(
            "Introduceti indexul,numele sau profesorul disciplinei pe care doriti sa o cautati: ")
        try:
            print(self.service.cauta_disciplina(intrare))
        except Eroare as ex:
            print(ex)


    def __s_generare(self):
        """
        Functia __s_generare genereaza studenti cu date aleatorii si ii adauga in catalog
        :return:
        """
        print("Introduceti numarul de studenti pe care doriti sa ii adaugati: ")
        intrare = input()
        try:
            self.service.genereaza_studenti(int(intrare))
        except Eroare as ex:
            print(ex)
        except ValueError as ve:
            print("Nu ati introdus un numar bun!")

    def __d_generare(self):
        """
        Functia __d_generare genereaza discipline cu date aleatorii si le adauga in catalog
        :return:
        """
        print("Introduceti numarul de discipline pe care doriti sa le adaugati: ")
        intrare = input()
        try:
            self.service.genereaza_discipline(int(intrare))
        except Eroare as ex:
            print(ex)
        except ValueError as ve:
            print("Nu ati introdus un numar bun!")

def run(console):
    """
    Ruleaza programul
    :return:
    """
    while True:

            print(console.meniu)
            comanda = input("Introduceti coamnda: ")
            if comanda in console.dict:
                if comanda == "adaugare":
                    print("Ce doriti sa adaugati?\nOptiuni posibile: student, disciplina, nota")
                    cmd = input()
                    console.dict[comanda][cmd]()
                elif comanda == "stergere":
                    print("Ce doriti sa stergeti?\nOptiuni posibile: student, disciplina, nota")
                    cmd = input()
                    console.dict[comanda][cmd]()
                elif comanda == "modificare":
                    print("Ce doriti sa modificati?\nOptiuni posibile: student, disciplina")
                    cmd = input()
                    console.dict[comanda][cmd]()
                elif comanda == "afisare":
                    print("Ce doriti sa afisati?\nOptiuni posibile: studenti, discipline, note")
                    cmd = input()
                    console.dict[comanda][cmd]()
                elif comanda == "cautare":
                    print("Ce doriti sa cautati?\nOptiuni posibile: student, disciplina")
                    cmd = input()
                    console.dict[comanda][cmd]()
                elif comanda == "generare":
                    print("Ce doriti sa generati?\nOptiuni posibile: student, disciplina")
                    cmd = input()
                    console.dict[comanda][cmd]()
                elif comanda == "statistici":
                    print("Ce doriti sa afisati?\nOptiuni posibile:\n1. Lista de studenți si notele lor la o disciplina data, ordonat: alfabetic dupa nume, dupa nota\n2. Primi 20% din studenti ordonat dupa media notelor la toate disciplinele (nume și nota)\n3. Afișați cei mai buni 20% studenți pentru o disciplină dată")
                    cmd = input()
                    console.dict[comanda][cmd]()
                elif comanda == "exit":
                    console.service.Repository.c1.storeToFile()
                    return


                else:
                    print("Nu exista comanda", comanda)
            else:
                print("Nu exista comanda", comanda)

