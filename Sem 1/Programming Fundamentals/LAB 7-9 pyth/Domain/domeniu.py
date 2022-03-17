class Student:
    """
    clasa Student
    """
    def __init__(self, iD, nume, prenume):
        """
        iD - int
        nume - str
        prenume - str
        :param iD:
        :param nume:
        :param prenume:
        """
        self.__id = iD
        self.__nume = nume
        self.__prenume = prenume
        self.discipline = {}

    def get_nume(self):
        return self.__nume

    def get_prenume(self):
        return self.__prenume

    def get_id(self):
        return self.__id

    def set_nume(self, nume):
        self.__nume = nume

    def set_prenume(self, prenume):
        self.__prenume = prenume

    def get_media(self):
        media = 0
        lu = 0
        for dis in self.discipline:
            if self.discipline[dis].get_media() != 0:
                media += self.discipline[dis].get_media()
                lu += 1
        if lu != 0:
            media /= lu
        return media

    def add_dis(self, disciplina):
        """
        Adauga o disciplina elevului
        disciplina - Disciplina()
        :param disciplina:
        :return:
        """
        self.discipline[disciplina.get_id()] = disciplina

    def del_dis(self, id):
        """
        Sterge disciplina cu id-ul id
        id - str
        :param id:
        :return:
        """
        del self.discipline[id]

    def add_n(self, disc, nota):
        """
        Adauaga nota (nota) la disciplina cu id-ul (disc)
        disc - str
        nota - int
        :param disc:
        :param nota:
        :return:
        """
        if disc in self.discipline:
            self.discipline[disc].add_nota(nota)
        else:
            raise Eroare("Disciplina inexistenta!")

    def del_n(self, disc, nota):
        """
        Sterge nota (nota) de la disciplina cu id-ul (disc)
        disc - str
        nota - int
        :param disc:
        :param nota:
        :return:
        """
        if disc in self.discipline:
            self.discipline[disc].del_nota(nota)
        else:
            raise Eroare("Disciplina inexistenta!")


    def __str__(self):
        mesaj = "id: " + str(self.get_id()) + "\n" + "nume: " + str(self.get_nume()) + ' ' + str(self.get_prenume())
        return mesaj


class Disciplina:
    """
    Clasa disciplina
    """
    def __init__(self, iD, nume, profesor):
        """
        iD - str
        nume - str
        prenume - str
        :param iD:
        :param nume:
        :param profesor:
        """
        self.__id = iD
        self.__nume = nume
        self.__profesor = profesor
        self.__note = []

    def get_nume(self):
        return self.__nume

    def get_profesor(self):
        return self.__profesor

    def get_id(self):
        return self.__id

    def get_note(self):
        return self.__note

    def get_media(self):
        media = 0
        for i in range(0, len(self.__note)):
            media += self.__note[i]
        try:
            media /= len(self.__note)
        except:
            return 0
        return media

    def set_nume(self, nume):
        self.__nume = nume

    def set_profesor(self, profesor):
        self.__profesor = profesor

    def set_id(self, id):
        self.__id = id

    def __str__(self):
        mesaj = "id: " + str(self.get_id()) + "\n" + "nume: " + str(self.get_nume()) + "\n" + "profesor: " + str(self.get_profesor())
        return mesaj

    def add_nota(self, nota):
        """
        Functia add_nota adauga nota (nota) in lista cu note
        nota - int
        :param nota:
        :return:
        """
        self.__note.append(nota)

    def del_nota(self, nota):
        """
        Functia del_nota sterge nota (nota) din lista cu note
        :param nota:
        :return:
        """
        ok = 0
        for i in range(0, len(self.__note)):
            if self.__note[i] == nota:
                self.__note.pop(i)
                ok = 1
                break
        if ok == 0:
            raise Eroare("Nota inexistenta!")


class Catalog:

    def __init__(self):
        self.ctl = {}
        self.discipline = {}
        self.v = Validator()

    def store(self, stud):
        """
        Memoreaza in catalog studentul stud
        stud - Student()
        :param stud:
        :return:
        """
        if stud.get_id() in self.ctl:
            raise Eroare("Id existent!")
        else:
            self.ctl[stud.get_id()] = stud
            for disc in self.discipline:
                new = Disciplina(self.discipline[disc].get_id(), self.discipline[disc].get_nume(), self.discipline[disc].get_profesor())
                self.ctl[stud.get_id()].add_dis(new)

    def delete(self, id):
        """
        Sterge din catalog studentul cu id-ul id
        id - int
        :param id:
        :return:
        """
        if id not in self.ctl:
            raise Eroare("Id inexistent!")
        else:
            del self.ctl[id]

    def afisare(self):
        """
        Afiseaza elevii din catalog
        :return:
        """
        if len(self.ctl) == 0:
            raise Eroare("Catalogul este gol")
        else:
            for elem in self.ctl:
                print(self.ctl[elem])
                print('')

    def add_disciplina(self, disc):
        """
        Adauga o disciplina in catalog si la fiecare student
        disc - Disciplina()
        :param disc:
        :return:
        """
        if disc.get_id() in self.discipline:
            raise Eroare("Id existent!")
        else:
            for elem in self.ctl:
                new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
                self.ctl[elem].add_dis(new)
            new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
            self.discipline[new.get_id()] = new

    def del_disciplina(self, id):
        """
        Sterge o disciplina din catalog si de la fiecare student
        id - str
        :param id:
        :return:
        """
        if id in self.discipline:
            del self.discipline[id]
            for elem in self.ctl:
                self.ctl[elem].del_dis(id)
        else:
            raise Eroare("Nu exista disciplina")

    def add_nota(self, id_s, id_d, nota):
        """
        Functia add_nota adauga nota nota elevului id_s la materia id_d
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].add_n(id_d, nota)

    def del_nota(self, id_s, id_d, nota):
        """
        Functia del_nota sterge nota nota elevului id_s de la materia id_d
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].del_n(id_d, nota)

    def modificare_d_nume(self, idi, nume):
        """
        Functia modificare_d_nume modifica numele disciplinei cu id-ul idi in nume
        idi - str
        nume - str
        :param idi:
        :param nume:
        :return:
        """
        try:
            self.v.validare_nume(nume)
            for stud in self.ctl:
                self.ctl[stud].discipline[idi].set_nume(nume)
            self.discipline[idi].set_nume(nume)
        except Eroare as ex:
            print(ex)

    def modificare_d_profesor(self, idi, profesor):
        """
        Functia modificare_d_profesor modifica numele profesorului cu id-ul idi in profesor
        idi - str
        profesor - str
        :param idi:
        :param profesor:
        :return:
        """
        try:
            self.v.validare_nume(profesor)
            for stud in self.ctl:
                self.ctl[stud].discipline[idi].set_profesor(profesor)
            self.discipline[idi].set_profesor(profesor)
        except Eroare as ex:
            print(ex)


class Validator:
    def __init__(self):
        pass

    def contine_simboluri(self, nume):
        """
        Verifica daca string-ul nume contine altceva in afara de litere si spatii
        nume - str
        :param nume:
        :return:
        """
        for i in range(0, len(nume)):
            if nume[i] < 'a' or nume[i] > 'z':
                if nume[i] < 'A' or nume[i] > 'Z':
                    if nume[i] != ' ':
                        return True
        return False

    def validare_s(self, id, nume, prenume):
        """
        valideaza studentul cu datele: id,nume,prenume
        id - int
        nume - str
        prenume - str
        :param id:
        :param nume:
        :param prenume:
        :return:
        """
        if id < 0 or id >= 999999999:
            raise Eroare("Indexul introdus nu este corect")
        if nume == '' or self.contine_simboluri(nume):
            raise Eroare("Numele introdus nu este corect")
        if prenume == '' or self.contine_simboluri(prenume):
            raise Eroare("Preumele introdus nu este corect")

    def validare_d(self, nume, profesor):
        """
        valideaza numele si profesorul unei discipline
        nume - str
        profesor - str
        :param nume:
        :param profesor:
        :return:
        """
        if nume == '' or self.contine_simboluri(nume):
            raise Eroare("Numele introdus nu este corect")
        if profesor == '' or self.contine_simboluri(profesor):
            raise Eroare("Numele introdus nu este corect")

    def validare_nume(self, nume):
        """
        Valideaza numele nume
        nume - str
        :param nume:
        :return:
        """
        if nume == '' or self.contine_simboluri(nume):
            raise Eroare("Numele introdus nu este corect")

    def validare_nota(self, nota):
        """
        Valideaza nota (nota)
        nota - int
        :param nota:
        :return:
        """
        if nota<1 or nota>10:
            raise Eroare("Nota nu se incadreaza in intervalul [1,10]")


class Eroare(Exception):
    """
    Clasa care primeste exceptiile
    """
    pass


class CatalogFisier:
    def __init__(self):
        """
        initializam noul catalog si incarcam in memorie studentii, disciplinele si notele existente in fisiere
        """
        self.ctl = {}
        self.discipline = {}
        self.v = Validator()

        studenti = self.__loadSFromFile()
        for st in studenti:
            self.ctl[st.get_id()] = st
            for disc in self.discipline:
                new = Disciplina(self.discipline[disc].get_id(), self.discipline[disc].get_nume(), self.discipline[disc].get_profesor())
                self.ctl[st.get_id()].add_dis(new)

        discipline = self.__loadDFromFile()
        for disc in discipline:
            for elem in self.ctl:
                new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
                self.ctl[elem].add_dis(new)
            new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
            self.discipline[new.get_id()] = new

        note = self.__loadNFromFile()
        for nt in note:
            self.add_notam(nt[0], nt[1], nt[2])

    def storeToFile(self):
        s = open("studenti.txt", "w")
        for st in self.ctl:
            string = str(self.ctl[st].get_id()) + ' ' + self.ctl[st].get_nume() + ' ' + self.ctl[st].get_prenume() + '\n'
            s.write(string)
        s.close()
        d = open("discipline.txt", "w")
        for ds in self.discipline:
            string = self.discipline[ds].get_id() + ', ' + self.discipline[ds].get_nume() + ', ' + self.discipline[ds].get_profesor() + '\n'
            d.write(string)
        d.close()

    def __loadNFromFile(self):
        try:
            n = open("note.txt", "r")
        except IOError:
            return []
        linen = n.readline().strip()
        rezn = []
        while linen != "":
            nota = linen.split(" ")
            nt = (int(nota[0]), nota[1], int(nota[2]))
            rezn.append(nt)
            linen = n.readline().strip()
        n.close()
        return rezn

    def __loadDFromFile(self):
        try:
            d = open("discipline.txt", "r")
        except IOError:
            return []
        lined = d.readline().strip()
        rezd = []
        while lined != "":
            disciplina = lined.split(", ")
            dis = Disciplina(disciplina[0], disciplina[1], disciplina[2])
            rezd.append(dis)
            lined = d.readline().strip()
        d.close()
        return rezd

    def __loadSFromFile(self):
        try:
            s = open("studenti.txt", "r")
        except IOError:
            return []
        lines = s.readline().strip()
        rezs = []
        while lines != "":
            student = lines.split(" ")
            st = Student(int(student[0]), student[1], student[2])
            rezs.append(st)
            lines = s.readline().strip()
        s.close()
        return rezs

    def __storeSToFile(self, students):
        """
        Incarca studentii in fila studenti.txt
        students - lista de clasa Student
        :param students:
        :return:
        """
        f = open("studenti.txt", "w")
        for st in students:
            string = str(st.get_id())+' '+st.get_nume()+' '+st.get_prenume()+'\n'
            f.write(string)
        f.close()

    def __storeNToFile(self, note):
        """
        Incarca notele in fila note.txt
        note - lista de liste cu detaliile notelor
        :param note:
        :return:
        """
        f = open("note.txt", "w")
        for nt in note:
            string = str(nt[0])+' '+nt[1]+' '+str(nt[2])+'\n'
            f.write(string)
        f.close()

    def __storeDToFile(self, discipline):
        """
        Incarca disciplinele in fila discipline.txt
        discipline - lista de clasa Disciplina
        :param discipline:
        :return:
        """
        f = open("discipline.txt", "w")
        for ds in discipline:
            string = ds.get_id()+', '+ds.get_nume()+', '+ds.get_profesor()+'\n'
            f.write(string)
        f.close()

    def store(self, stud):
        """
        Memoreaza in catalog studentul stud
        stud - Student()
        :param stud:
        :return:
        """
        if stud.get_id() in self.ctl:
            raise Eroare("Id existent!")
        else:
            self.ctl[stud.get_id()] = stud
            for disc in self.discipline:
                new = Disciplina(self.discipline[disc].get_id(), self.discipline[disc].get_nume(), self.discipline[disc].get_profesor())
                self.ctl[stud.get_id()].add_dis(new)

    def delete(self, id):
        """
        Sterge din catalog studentul cu id-ul id
        id - int
        :param id:
        :return:
        """
        if id not in self.ctl:
            raise Eroare("Id inexistent!")
        else:
            del self.ctl[id]
            alls = self.__loadSFromFile()
            for i in range(0, len(alls)):
                if alls[i].get_id() == id:
                    alls.pop(i)
            self.__storeSToFile(alls)
            alln = self.__loadNFromFile()
            for i in range(0, len(alln)):
                if alln[i][0] == id:
                    alln.pop(i)
            self.__storeNToFile(alln)

    def add_disciplina(self, disc):
        """
        Adauga o disciplina in catalog si la fiecare student
        disc - Disciplina()
        :param disc:
        :return:
        """
        if disc.get_id() in self.discipline:
            raise Eroare("Id existent!")
        else:
            for elem in self.ctl:
                new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
                self.ctl[elem].add_dis(new)
            new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
            self.discipline[new.get_id()] = new

    def del_disciplina(self, id):
        """
        Sterge o disciplina din catalog si de la fiecare student
        id - str
        :param id:
        :return:
        """
        if id in self.discipline:
            del self.discipline[id]
            alld = self.__loadDFromFile()
            for i in range(0, len(alld)):
                if alld[i].get_id() == id:
                    alld.pop(i)
            self.__storeDToFile(alld)
            alln = self.__loadNFromFile()
            for i in range(0, len(alln)):
                if alln[i][1] == id:
                    alln.pop(i)
            self.__storeNToFile(alln)
            for elem in self.ctl:
                self.ctl[elem].del_dis(id)
        else:
            raise Eroare("Nu exista disciplina")

    def afisare(self):
        """
        Afiseaza elevii din catalog
        :return:
        """
        if len(self.ctl) == 0:
            raise Eroare("Catalogul este gol")
        else:
            for elem in self.ctl:
                print(self.ctl[elem])
                print('')

    def add_nota(self, id_s, id_d, nota):
        """
        Functia add_nota adauga nota nota elevului id_s la materia id_d si in fisier
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].add_n(id_d, nota)
        alln = self.__loadNFromFile()
        alln.append((id_s, id_d, nota))
        self.__storeNToFile(alln)

    def add_notam(self, id_s, id_d, nota):
        """
        Functia add_nota adauga nota nota elevului id_s la materia id_d doar in memorie
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].add_n(id_d, nota)

    def del_nota(self, id_s, id_d, nota):
        """
        Functia add_nota sterge nota nota elevului id_s de la materia id_d
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].del_n(id_d, nota)
        alln = self.__loadNFromFile()
        for i in range(0, len(alln)):
            if alln[i][1] == id_d and alln[i][2] == nota:
                alln.pop(i)
        self.__storeNToFile(alln)

    def modificare_d_nume(self, idi, nume):
        """
        Functia modificare_d_nume modifica numele disciplinei cu id-ul idi in nume
        idi - str
        nume - str
        :param idi:
        :param nume:
        :return:
        """
        try:
            self.v.validare_nume(nume)
            for stud in self.ctl:
                self.ctl[stud].discipline[idi].set_nume(nume)
            self.discipline[idi].set_nume(nume)
        except Eroare as ex:
            print(ex)

    def modificare_d_profesor(self, idi, profesor):
        """
        Functia modificare_d_profesor modifica numele profesorului cu id-ul idi in profesor
        idi - str
        profesor - str
        :param idi:
        :param profesor:
        :return:
        """
        try:
            self.v.validare_nume(profesor)
            for stud in self.ctl:
                self.ctl[stud].discipline[idi].set_profesor(profesor)
            self.discipline[idi].set_profesor(profesor)
        except Eroare as ex:
            print(ex)


class DTO1:
    def __init__(self, stud, dis):
        self.nume = stud.get_nume()+' '+stud.get_prenume()
        self.note = stud.discipline[dis].get_note()
        self.media = stud.discipline[dis].get_media()


class DTO2:
    def __init__(self, stud):
        self.nume = stud.get_nume()+' '+stud.get_prenume()
        self.media = stud.get_media()


class CatalogFisier2:
    def __init__(self):
        """
        initializam noul catalog si incarcam in memorie studentii, disciplinele si notele existente in fisiere
        """
        self.ctl = {}
        self.v = Validator()

        studenti = self.__loadSFromFile()
        for st in studenti:
            self.ctl[st.get_id()] = st
            try:
                d = open("discipline.txt", "r")
            except IOError:
                d = []
            lined = d.readline().strip()
            while lined != "":
                disciplina = lined.split(", ")
                dis = Disciplina(disciplina[0], disciplina[1], disciplina[2])
                self.ctl[st.get_id()].add_dis(dis)
                lined = d.readline().strip()
            d.close()


        note = self.__loadNFromFile()
        for nt in note:
            try:
                self.add_notam(nt[0], nt[1], nt[2])
            except:
                alln = self.__loadNFromFile()
                for i in range(0, len(alln)):
                    if alln[i][1] == id:
                        alln.pop(i)
                self.__storeNToFile(alln)

    def storeToFile(self):
        s = open("studenti.txt", "w")
        for st in self.ctl:
            string = str(self.ctl[st].get_id()) + ' ' + self.ctl[st].get_nume() + ' ' + self.ctl[st].get_prenume() + '\n'
            s.write(string)
        s.close()

    def __loadNFromFile(self):
        try:
            n = open("note.txt", "r")
        except IOError:
            return []
        linen = n.readline().strip()
        rezn = []
        while linen != "":
            nota = linen.split(" ")
            nt = (int(nota[0]), nota[1], int(nota[2]))
            rezn.append(nt)
            linen = n.readline().strip()
        n.close()
        return rezn

    def __loadSFromFile(self):
        try:
            s = open("studenti.txt", "r")
        except IOError:
            return []
        lines = s.readline().strip()
        rezs = []
        while lines != "":
            student = lines.split(" ")
            st = Student(int(student[0]), student[1], student[2])
            rezs.append(st)
            lines = s.readline().strip()
        s.close()
        return rezs

    def __storeSToFile(self, students):
        """
        Incarca studentii in fila studenti.txt
        students - lista de clasa Student
        :param students:
        :return:
        """
        f = open("studenti.txt", "w")
        for st in students:
            string = str(st.get_id())+' '+st.get_nume()+' '+st.get_prenume()+'\n'
            f.write(string)
        f.close()

    def __storeNToFile(self, note):
        """
        Incarca notele in fila note.txt
        note - lista de liste cu detaliile notelor
        :param note:
        :return:
        """
        f = open("note.txt", "w")
        for nt in note:
            string = str(nt[0])+' '+nt[1]+' '+str(nt[2])+'\n'
            f.write(string)
        f.close()

    def store(self, stud):
        """
        Memoreaza in catalog studentul stud
        stud - Student()
        :param stud:
        :return:
        """
        if stud.get_id() in self.ctl:
            raise Eroare("Id existent!")
        else:
            self.ctl[stud.get_id()] = stud
            try:
                d = open("discipline.txt", "r")
            except IOError:
                d = []
            lined = d.readline().strip()
            while lined != "":
                disciplina = lined.split(", ")
                dis = Disciplina(disciplina[0], disciplina[1], disciplina[2])
                self.ctl[stud.get_id()].add_dis(dis)
                lined = d.readline().strip()
            d.close()

    def delete(self, id):
        """
        Sterge din catalog studentul cu id-ul id
        id - int
        :param id:
        :return:
        """
        if id not in self.ctl:
            raise Eroare("Id inexistent!")
        else:
            del self.ctl[id]
            alls = self.__loadSFromFile()
            for i in range(0, len(alls)):
                if alls[i].get_id() == id:
                    alls.pop(i)
            self.__storeSToFile(alls)
            alln = self.__loadNFromFile()
            for i in range(0, len(alln)):
                if alln[i][0] == id:
                    alln.pop(i)
            self.__storeNToFile(alln)

    def add_disciplina(self, disc):
        """
        Adauga o disciplina in catalog si la fiecare student
        disc - Disciplina()
        :param disc:
        :return:
        """
        try:
            d = open("discipline.txt", "r")
        except IOError:
            d = []
        lined = d.readline().strip()
        while lined != "":
            disciplina = lined.split(", ")
            dis = Disciplina(disciplina[0], disciplina[1], disciplina[2])
            if disc.get_id == dis.get_id:
                raise Eroare("Id existent!")
            lined = d.readline().strip()
        d.close()
        for elem in self.ctl:
            new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
            self.ctl[elem].add_dis(new)
        new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
        f = open("discipline.txt", "a")
        string = new.get_id() + ', ' + new.get_nume() + ', ' + new.get_profesor() + '\n'
        f.write(string)
        f.close()

    def del_disciplina(self, id):
        """
        Sterge o disciplina din catalog si de la fiecare student
        id - str
        :param id:
        :return:
        """
        ok = 0
        try:
            d = open("discipline.txt", "r")
        except IOError:
            d = []
        lined = d.readline().strip()
        t = open("temporar.txt", "w")
        while lined != "":
            disciplina = lined.split(", ")
            dis = Disciplina(disciplina[0], disciplina[1], disciplina[2])
            if id == dis.get_id:
                alln = self.__loadNFromFile()
                for i in range(0, len(alln)):
                    if alln[i][1] == id:
                        alln.pop(i)
                self.__storeNToFile(alln)
                for elem in self.ctl:
                    self.ctl[elem].del_dis(id)
                ok = 1
            else:
                #adaugam la fisierul temporar
                t.write(lined)
            lined = d.readline().strip()
        t.close()
        d.close()
        if ok == 1:

            t = open("temporar.txt", "r")
            d = open("discipline.txt", "w")

            content = t.read()
            d.write(content)
            d.close()
            t.close()
        else:
            raise Eroare("Disciplina inexistenta")

    def afisare(self):
        """
        Afiseaza elevii din catalog
        :return:
        """
        if len(self.ctl) == 0:
            raise Eroare("Catalogul este gol")
        else:
            for elem in self.ctl:
                print(self.ctl[elem])
                print('')

    def add_nota(self, id_s, id_d, nota):
        """
        Functia add_nota adauga nota nota elevului id_s la materia id_d si in fisier
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].add_n(id_d, nota)
        alln = self.__loadNFromFile()
        alln.append((id_s, id_d, nota))
        self.__storeNToFile(alln)

    def add_notam(self, id_s, id_d, nota):
        """
        Functia add_nota adauga nota nota elevului id_s la materia id_d doar in memorie
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].add_n(id_d, nota)

    def del_nota(self, id_s, id_d, nota):
        """
        Functia add_nota sterge nota nota elevului id_s de la materia id_d
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].del_n(id_d, nota)
        alln = self.__loadNFromFile()
        for i in range(0, len(alln)):
            if alln[i][1] == id_d and alln[i][2] == nota:
                alln.pop(i)
        self.__storeNToFile(alln)

    def modificare_d_nume(self, idi, nume):
        """
        Functia modificare_d_nume modifica numele disciplinei cu id-ul idi in nume
        idi - str
        nume - str
        :param idi:
        :param nume:
        :return:
        """
        try:
            self.v.validare_nume(nume)
            for stud in self.ctl:
                self.ctl[stud].discipline[idi].set_nume(nume)
            ok = 0
            try:
                d = open("discipline.txt", "r")
            except IOError:
                d = []
            lined = d.readline().strip()
            t = open("temporar.txt", "w")
            while lined != "":
                disciplina = lined.split(", ")
                dis = Disciplina(disciplina[0], disciplina[1], disciplina[2])
                if idi == dis.get_id():
                    lined = dis.get_id() + ', ' + nume + ', ' + dis.get_profesor()
                    ok = 1
                lined = lined + "\n"
                t.write(lined)
                lined = d.readline().strip()
            t.close()
            d.close()
            if ok == 1:

                t = open("temporar.txt", "r")
                d = open("discipline.txt", "w")

                content = t.read()
                d.write(content)
                d.close()
                t.close()
            else:
                raise Eroare("Disciplina inexistenta")
        except Eroare as ex:
            print(ex)

    def modificare_d_profesor(self, idi, profesor):
        """
        Functia modificare_d_profesor modifica numele profesorului cu id-ul idi in profesor
        idi - str
        profesor - str
        :param idi:
        :param profesor:
        :return:
        """
        try:
            self.v.validare_nume(profesor)
            for stud in self.ctl:
                self.ctl[stud].discipline[idi].set_profesor(profesor)
            ok = 0
            try:
                d = open("discipline.txt", "r")
            except IOError:
                d = []
            lined = d.readline().strip()
            t = open("temporar.txt", "w")
            while lined != "":
                disciplina = lined.split(", ")
                dis = Disciplina(disciplina[0], disciplina[1], disciplina[2])
                if idi == dis.get_id():
                    lined = disciplina[0] + ", " + disciplina[1] + ", " + profesor
                    ok = 1
                lined = lined + "\n"
                t.write(lined)
                lined = d.readline().strip()
            t.close()
            d.close()
            if ok == 1:

                t = open("temporar.txt", "r")
                d = open("discipline.txt", "w")

                content = t.read()
                d.write(content)
                d.close()
                t.close()
            else:
                raise Eroare("Disciplina inexistenta")
        except Eroare as ex:
            print(ex)

class CatalogFisier3:
    def __init__(self):
        """
        initializam noul catalog si incarcam in memorie studentii, disciplinele si notele existente in fisiere
        """
        self.ctl = {}
        self.v = Validator()

        self.incarcareStudentiCuDis()

        note = self.__loadNFromFile()
        for nt in note:
            self.add_notam(nt[0], nt[1], nt[2])

    def incarcareStudentiCuDis(self):
        studenti = self.__loadSFromFile()
        for st in studenti:
            self.ctl[st.get_id()] = st
            discipline = self.__loadDFromFile()
            for disc in discipline:
                self.ctl[st.get_id()].add_dis(disc)

    def storeToFile(self):
        s = open("studenti.txt", "w")
        for st in self.ctl:
            string = str(self.ctl[st].get_id()) + ' ' + self.ctl[st].get_nume() + ' ' + self.ctl[st].get_prenume() + '\n'
            s.write(string)
        s.close()

    def __loadNFromFile(self):
        try:
            n = open("note.txt", "r")
        except IOError:
            return []
        linen = n.readline().strip()
        rezn = []
        while linen != "":
            nota = linen.split(" ")
            nt = (int(nota[0]), nota[1], int(nota[2]))
            rezn.append(nt)
            linen = n.readline().strip()
        n.close()
        return rezn

    def __loadDFromFile(self):
        try:
            d = open("discipline.txt", "r")
        except IOError:
            return []
        lined = d.readline().strip()
        rezd = []
        while lined != "":
            disciplina = lined.split(", ")
            dis = Disciplina(disciplina[0], disciplina[1], disciplina[2])
            rezd.append(dis)
            lined = d.readline().strip()
        d.close()
        return rezd

    def __loadSFromFile(self):
        try:
            s = open("studenti.txt", "r")
        except IOError:
            return []
        lines = s.readline().strip()
        rezs = []
        while lines != "":
            student = lines.split(" ")
            st = Student(int(student[0]), student[1], student[2])
            rezs.append(st)
            lines = s.readline().strip()
        s.close()
        return rezs

    def __storeSToFile(self, students):
        """
        Incarca studentii in fila studenti.txt
        students - lista de clasa Student
        :param students:
        :return:
        """
        f = open("studenti.txt", "w")
        for st in students:
            string = str(st.get_id())+' '+st.get_nume()+' '+st.get_prenume()+'\n'
            f.write(string)
        f.close()

    def __storeNToFile(self, note):
        """
        Incarca notele in fila note.txt
        note - lista de liste cu detaliile notelor
        :param note:
        :return:
        """
        f = open("note.txt", "w")
        for nt in note:
            string = str(nt[0])+' '+nt[1]+' '+str(nt[2])+'\n'
            f.write(string)
        f.close()

    def __storeDToFile(self, discipline):
        """
        Incarca disciplinele in fila discipline.txt
        discipline - lista de clasa Disciplina
        :param discipline:
        :return:
        """
        f = open("discipline.txt", "w")
        for ds in discipline:
            string = ds.get_id()+', '+ds.get_nume()+', '+ds.get_profesor()+'\n'
            f.write(string)
        f.close()

    def store(self, stud):
        """
        Memoreaza in catalog studentul stud
        stud - Student()
        :param stud:
        :return:
        """
        if stud.get_id() in self.ctl:
            raise Eroare("Id existent!")
        else:
            self.ctl[stud.get_id()] = stud
            discipline = self.__loadDFromFile()
            for disc in discipline:
                self.ctl[stud.get_id()].add_dis(disc)

    def delete(self, id):
        """
        Sterge din catalog studentul cu id-ul id
        id - int
        :param id:
        :return:
        """
        if id not in self.ctl:
            raise Eroare("Id inexistent!")
        else:
            del self.ctl[id]
            alls = self.__loadSFromFile()
            for i in range(0, len(alls)):
                if alls[i].get_id() == id:
                    alls.pop(i)
            self.__storeSToFile(alls)
            alln = self.__loadNFromFile()
            for i in range(0, len(alln)):
                if alln[i][0] == id:
                    alln.pop(i)
            self.__storeNToFile(alln)

    def add_disciplina(self, disc):
        """
        Adauga o disciplina in catalog si la fiecare student
        disc - Disciplina()
        :param disc:
        :return:
        """
        discipline = self.__loadDFromFile()
        if disc in discipline:
            raise Eroare("Id existent!")
        else:
            for elem in self.ctl:
                new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
                self.ctl[elem].add_dis(new)
            new = Disciplina(disc.get_id(), disc.get_nume(), disc.get_profesor())
            discipline.append(new)
            self.__storeDToFile(discipline)

    def del_disciplina(self, id):
        """
        Sterge o disciplina din catalog si de la fiecare student
        id - str
        :param id:
        :return:
        """
        ok = 0
        discipline = self.__loadDFromFile()
        for i in range(0,len(discipline)):
            if discipline[i].get_id() == id:
                alld = self.__loadDFromFile()
                for i in range(0, len(alld)):
                    if alld[i].get_id() == id:
                        alld.pop(i)
                self.__storeDToFile(alld)
                alln = self.__loadNFromFile()
                for i in range(0, len(alln)):
                    if alln[i][1] == id:
                        alln.pop(i)
                self.__storeNToFile(alln)
                for elem in self.ctl:
                    self.ctl[elem].del_dis(id)
                ok = 1
        if ok == 0:
            raise Eroare("Nu exista disciplina")

    def afisare(self):
        """
        Afiseaza elevii din catalog
        :return:
        """
        if len(self.ctl) == 0:
            raise Eroare("Catalogul este gol")
        else:
            for elem in self.ctl:
                print(self.ctl[elem])
                print('')

    def add_nota(self, id_s, id_d, nota):
        """
        Functia add_nota adauga nota nota elevului id_s la materia id_d si in fisier
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].add_n(id_d, nota)
        alln = self.__loadNFromFile()
        alln.append((id_s, id_d, nota))
        self.__storeNToFile(alln)
        self.incarcareStudentiCuDis()

    def add_notam(self, id_s, id_d, nota):
        """
        Functia add_nota adauga nota nota elevului id_s la materia id_d doar in memorie
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].add_n(id_d, nota)

    def del_nota(self, id_s, id_d, nota):
        """
        Functia add_nota sterge nota nota elevului id_s de la materia id_d
        id_s - int
        id_d - str
        nota - int
        :param id_s:
        :param id_d:
        :param nota:
        :return:
        """
        self.ctl[id_s].del_n(id_d, nota)
        alln = self.__loadNFromFile()
        for i in range(0, len(alln)):
            if alln[i][1] == id_d and alln[i][2] == nota:
                alln.pop(i)
        self.__storeNToFile(alln)
        self.incarcareStudentiCuDis()

    def modificare_d_nume(self, idi, nume):
        """
        Functia modificare_d_nume modifica numele disciplinei cu id-ul idi in nume
        idi - str
        nume - str
        :param idi:
        :param nume:
        :return:
        """
        discipline = self.__loadDFromFile()
        try:
            self.v.validare_nume(nume)
            for stud in self.ctl:
                self.ctl[stud].discipline[idi].set_nume(nume)
            for i in range(0, len(discipline)):
                if discipline[i].get_id() == idi:
                    discipline[i].set_nume(nume)
            self.__storeDToFile(discipline)
        except Eroare as ex:
            print(ex)

    def modificare_d_profesor(self, idi, profesor):
        """
        Functia modificare_d_profesor modifica numele profesorului cu id-ul idi in profesor
        idi - str
        profesor - str
        :param idi:
        :param profesor:
        :return:
        """
        discipline = self.__loadDFromFile()
        try:
            self.v.validare_nume(profesor)
            for stud in self.ctl:
                self.ctl[stud].discipline[idi].set_profesor(profesor)
            for i in range(0, len(discipline)):
                if discipline[i].get_id() == idi:
                    discipline[i].set_profesor(profesor)
            self.__storeDToFile(discipline)
        except Eroare as ex:
            print(ex)
