from Repository.repos import *
import string
import random

class Service:

    def __init__(self, repos):
        """
        Se initializeaza Repository-ul pentru catalog
        :param repos, de tipul Repository():
        """
        self.Repository = repos

    def adauga_student(self, id, nume, prenume):
        """
        Se adauga studentul cu datele: id, nume, prenume
        id - int
        nume - str
        prenume - str
        :param id:
        :param nume:
        :param prenume:
        :return:
        """
        try:
            self.Repository.adaugare_s(id, nume, prenume)
            print("Studentul a fost adaugat!")
        except Eroare as ex:
            print(ex)

    def adauga_disciplina(self, id, nume, profesor):
        """
        Se adauga disciplina cu datele: id, nume, profesor
        id - str
        nume - str
        profesor - str
        :param id:
        :param nume:
        :param profesor:
        :return:
        """
        try:
            self.Repository.adaugare_d(id, nume, profesor)
            print("Disciplina a fost adaugata!")
        except Eroare as ex:
            print(ex)

    def sterge_student(self, id):
        """
        Se sterge studentul cu id-ul "id"
        id - int
        :param id:
        :return:
        """
        try:
            self.Repository.stergere_s(id)
            print("Studentul a fost sters!")
        except Eroare as ex:
            print(ex)

    def sterge_disciplina(self, id):
        """
        Se sterge disciplina cu id-ul "id"
        id - str
        :param id:
        :return:
        """
        try:
            self.Repository.stergere_d(id)
            print("Disciplina a fost stearsa!")
        except Eroare as ex:
            print(ex)

    def afiseaza_studenti(self):
        """
        Afiseaza studentii catalogului
        :return:
        """
        try:
            self.Repository.afisare_c()
        except Eroare as ex:
            print(ex)

    def afiseaza_discipline(self):
        """
        Afiseaza disciplinele
        :return:
        """
        try:
            self.Repository.afisare_d()
        except Eroare as ex:
            print(ex)

    def cauta_student(self, srch):
        """
        Functia cauta_student cauta in repository si returneaza date despre studentul gasit, cautand intai dupa id iar mai apoi dupa nume
        srch - str
        :param srch:
        :return:
        """
        mesaj = ""
        for id in self.Repository.c1.ctl:
            try:
                if id == int(srch):
                    mesaj += str(self.Repository.c1.ctl[id])
            except:
                if self.Repository.c1.ctl[id].get_nume() == srch:
                    mesaj += str(self.Repository.c1.ctl[id]) +"\n"
        if mesaj == "":
            return "Nu a fost gasit elevul "+str(srch)
        else:
            return mesaj

    def cauta_disciplina(self, srch):
        """
        Functia cauta_disciplina cauta in repository si returneaza date despre disciplina gasita, cautand intai dupa id iar mai apoi dupa nume si profesor
        srch - str
        :param srch:
        :return:
        """
        mesaj = ""
        student_temporar = Student(999999999, "test", "bot")
        self.Repository.c1.store(student_temporar)
        for id in self.Repository.c1.ctl[999999999].discipline:
            if id == srch:
                mesaj += str(self.Repository.c1.ctl[999999999].discipline[id])
            elif self.Repository.c1.ctl[999999999].discipline[id].get_nume() == srch:
                mesaj += str(self.Repository.c1.ctl[999999999].discipline[id]) + "\n"
            elif self.Repository.c1.ctl[999999999].discipline[id].get_profesor() == srch:
                mesaj += str(self.Repository.c1.ctl[999999999].discipline[id]) + "\n"
        self.Repository.c1.delete(999999999)
        if mesaj == "":
            return "Nu a fost gasita disciplina "+srch
        else:
            return mesaj

    def adauga_nota(self, id_s, id_d, nota):
        """
        Functia adauga_nota adauga nota (nota) studentului cu indexul id_s la materia cu indexul id_d
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        if id_s in self.Repository.c1.ctl:
            self.Repository.c1.add_nota(id_s, id_d, nota)
        else:
            raise Eroare("Student inexistent!")

    def sterge_nota(self, id_s, id_d, nota):
        """
        Functia sterge_nota sterge nota (nota) studentului cu indexul id_s de la materia cu indexul id_d
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        if id_s not in self.Repository.c1.ctl:
            raise Eroare("Id inexistent!")
        else:
            self.Repository.c1.del_nota(id_s, id_d, nota)

    def afiseaza_note(self, id):
        """
        Functia afiseaza note afiseaza notele elevului cu id-ul id
        id - int
        :param id:
        :return:
        """
        if id not in self.Repository.c1.ctl:
            raise Eroare("Id inexistent")
        else:
            self.Repository.afisare_n(id)

    def generare_date_student(self):
        """
        Functia generare_date_student genereaza date aleatorii despre un student si il adauga in catalog
        :return:
        """
        alfabet = string.ascii_lowercase
        numere = string.digits
        nume = ''.join(random.choice(alfabet) for i in range(6))
        prenume = ''.join(random.choice(alfabet) for i in range(6))
        id = ''.join(random.choice(numere) for i in range(4))
        self.Repository.adaugare_s(int(id), nume, prenume)
        print("Studentul a fost adaugat!")
    #recursiv
    def genereaza_studenti(self, n):
        """
        Fucntia genereaza_studenti genereaza n studenti cu date aleatorii si ii adauga in catalog
        n - int
        :param n:
        :return:
        """
        if n > 0:
            try:
                self.generare_date_student()
            except:
                n = n - 1
            self.genereaza_studenti(n-1)


    def generare_date_disciplina(self):
        """
        Functia generare_date_disciplina genereaza date aleatorii despre o disciplina si o adauga in catalog
        :return:
        """
        alfabet = string.ascii_lowercase
        numere = string.digits
        nume = ''.join(random.choice(alfabet) for i in range(6))
        profesor = ''.join(random.choice(alfabet) for i in range(6))
        profesor = profesor + ' '
        profesor_prenume = ''.join(random.choice(alfabet) for i in range(6))
        profesor = profesor + profesor_prenume
        id = ''.join(random.choice(numere) for i in range(4))
        self.Repository.adaugare_d(id, nume, profesor)
        print("Disciplina a fost adaugata!")
    #recursiv
    def genereaza_discipline(self, n):
        """
        Functia genereaza_discipline genereaza n discipline cu date aleatorii si le adauga in catalog
        n - int
        :param n:
        :return:
        """
        if n>0:
            try:
                self.generare_date_disciplina()
            except:
                n = n + 1
            self.genereaza_discipline(n-1)

    def afiseaza_ordonat(self, id, what):
        """
        Functia afiseaza_ordonat ordoneaza lista de studenti dupa nota sau dupa nume si ii afiseaza
        what este dupa ce se sorteaza lista ( nume sau note)
        id - str
        what - str
        :param id:
        :param what:
        :return:
        """
        student_temporar = Student(999999999, "test", "bot")
        self.Repository.c1.store(student_temporar)
        if id in self.Repository.c1.ctl[999999999].discipline:
            self.Repository.c1.delete(999999999)
            lista = self.Repository.get_dto1(id)
            if what == "nume":
                #lista = self.ShakeSort(lista, key=lambda student: student.nume)
                lista = self.ShakeSort(lista, cmp=self.cmp_nume_grt)
            elif what == "nota":
                #lista= self.ShakeSort(lista, key=lambda student: student.media)
                lista = self.ShakeSort(lista, cmp=self.cmp_media_grt)

            else:
                print("Nu ati introdus o optiune valida!")
        else:
            self.Repository.c1.delete(999999999)
            lista = []
        return lista

    def afiseaza_top_dis(self, disciplina):
        """
        Functia afiseaza_top ordoneaza studentii dupa media lor la disciplina dis si ii afiseaza pe primii 20%
        :return:
        """
        lista = []
        student_temporar = Student(999999999, "test", "bot")
        self.Repository.c1.store(student_temporar)
        if disciplina in self.Repository.c1.ctl[999999999].discipline:
            for ident in self.Repository.c1.ctl:
                lista.append(self.Repository.c1.ctl[ident])
            #lista.sort(reverse=True, key=lambda stud: stud.discipline[disciplina].get_media())
            lista = self.SelectionSort(lista, key=lambda stud: stud.discipline[disciplina].get_media(), reverse=True)
        else:
            raise Eroare("Nu exista disciplina")
        self.Repository.c1.delete(999999999)
        return lista

    def cmp_media_grt(self, stud1, stud2):
        if stud1.media > stud2.media:
            return True
        return False

    def cmp_nume_grt(self, stud1, stud2):
        if stud1.nume > stud2.nume:
            return True
        return False

    def cmp_media_nume_lss(self, stud1, stud2):
        if stud1.media < stud2.media:
            return True
        elif stud1.media == stud2.media:
            if stud1.nume < stud2.nume:
                return True
        return False

    def afiseaza_top(self):
        """
        Functia afiseaza_top ordoneaza studentii dupa media lor generala si ii afiseaza pe primii 20%
        :return:
        """
        lista = self.Repository.get_dto2()
        #lista.sort(reverse=True, key=lambda student: student.media)
        #lista = self.ShakeSort(lista, key=lambda student: student.media, reverse=True)
        lista = self.SelectionSort(lista, cmp=self.cmp_media_nume_lss, reverse=True)
        return lista

    def SelectionSort(self, lis, key=lambda x: x, reverse=False, cmp=lambda x, y: x < y):
        """
        sorteaza elementele unei liste
        lis - list
        returneaza lista ordonata (l[0]<l[1]<...)
        """
        for i in range(0, len(lis) - 1):
            ind = i
            # find the smallest element in the rest of the list
            for j in range(i + 1, len(lis)):
                if cmp(key(lis[j]), key(lis[ind])):
                    ind = j
            if (i < ind):
                # interchange
                aux = lis[i]
                lis[i] = lis[ind]
                lis[ind] = aux
        if reverse:
            reversed_list = lis[::-1]
            return reversed_list
        return lis

    def ShakeSort(self, lis, key=lambda x: x, reverse=False, cmp=lambda x, y: x > y):
        """
        sorteaza elementele unei liste
        lis - list
        returneaza lista ordonata (l[0]<l[1]<...)
        """
        n = len(lis)
        swapped = True
        start = 0
        end = n - 1
        while (swapped == True):
            swapped = False
            for i in range(start, end):
                if cmp(key(lis[i]), key(lis[i + 1])):
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
                    swapped = True
            if (swapped == False):
                break
            swapped = False
            end = end - 1
            for i in range(end - 1, start - 1, -1):
                if cmp(key(lis[i]), key(lis[i + 1])):
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
                    swapped = True
            start = start + 1
        if reverse:
            reversed_list = lis[::-1]
            return reversed_list
        return lis

