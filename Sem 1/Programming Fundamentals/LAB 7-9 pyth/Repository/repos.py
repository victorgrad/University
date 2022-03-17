from Domain.domeniu import *


class Repos:
    """
    Ropsitory
    """
    def __init__(self, catalog, validator):
        self.c1 = catalog
        self.v = validator

    def adaugare_s(self, id, nume, prenume):
        """
        Functia adaugare_s adauga studentul cu id-ul id numele nume si prenumele prenume in catalog
        id - int
        nume - str
        prenume - str
        :param id:
        :param nume:
        :param prenume:
        :return:
        """
        self.v.validare_s(id, nume, prenume)
        el = Student(id, nume, prenume)
        self.c1.store(el)

    def stergere_s(self, id):
        """
        Functia stergere_s sterge elevul din catalog cu id-ul id
        id - int
        :param id:
        :return:
        """
        self.c1.delete(id)

    def adaugare_d(self, id, nume, profesor):
        """
        Fucntia adaugare_d adauga disciplina cu id-ul id numele nume si profesorul profesor in catalog
        id - str
        nume - str
        profesor - str
        :param id:
        :param nume:
        :param profesor:
        :return:
        """
        if id == '':
            raise Eroare("Id invalid")
        self.v.validare_d(nume, profesor)
        dis = Disciplina(id, nume, profesor)
        self.c1.add_disciplina(dis)

    def stergere_d(self, id):
        """
        Functia stergere_d sterge disciplina cu id-ul id din catalog
        id - str
        :param id:
        :return:
        """
        self.c1.del_disciplina(id)


    def afisare_c(self):
        """
        Functia afisare_c afiseaza elevii catalogului
        :return:
        """
        self.c1.afisare()


    def afisare_d(self):
        """
        Functia afisare_d afiseaza disciplinele catalogului
        :return:
        """
        student_temporar = Student(999999999, "test", "bot")
        self.c1.store(student_temporar)
        for dis in self.c1.ctl[999999999].discipline:
            print(self.c1.ctl[999999999].discipline[dis])
            print('')
        self.c1.delete(999999999)

    def modificare_s_nume(self, idi, nume):
        """
        Functia modificare_s_nume modifica numele studentului cu id-ul id in nume
        idi - int
        nume - str
        :param idi:
        :param nume:
        :return:
        """
        try:
            self.v.validare_nume(nume)
            self.c1.ctl[idi].set_nume(nume)
        except Eroare as ex:
            print(ex)

    def modificare_s_prenume(self, idi, prenume):
        """
        Functia modificare_s_prenume modifica prenumele studentului cu id-ul id in prenume
        idi - int
        prenume - str
        :param idi:
        :param prenume:
        :return:
        """
        try:
            self.v.validare_nume(prenume)
            self.c1.ctl[idi].set_prenume(prenume)
        except Eroare as ex:
            print(ex)

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
            self.c1.modificare_d_nume(idi, nume)
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
            self.c1.modificare_d_profesor(idi, profesor)
        except Eroare as ex:
            print(ex)

    def afisare_n(self, id):
        """
        Functia afisare_n afiseaza notele studentului de la id-ul id
        id - int
        :param id:
        :return:
        """
        print(self.c1.ctl[id].get_nume(), self.c1.ctl[id].get_prenume(), ':')
        for disc in self.c1.ctl[id].discipline:
            print("materia: ", self.c1.ctl[id].discipline[disc].get_nume(), "\nprofesorul: ", self.c1.ctl[id].discipline[disc].get_profesor(), "\nnotele: ", self.c1.ctl[id].discipline[disc].get_note(), "\n")

    def get_dto1(self, dis):
        """
        Functia get_dto1 preia o materie si si creeaza o lista cu toti studentii, notele si mediile acestora la disciplina dis
        dis = str
        :param dis:
        :return:
        """
        lista = []
        for stud in self.c1.ctl:
            dto = DTO1(self.c1.ctl[stud], dis)
            lista.append(dto)
        return lista

    def get_dto2(self):
        """
        Functia get_dto2  creeaza o lista cu toti studentii si mediile lor generale
        :return:
        """
        lista = []
        for stud in self.c1.ctl:
            dto = DTO2(self.c1.ctl[stud])
            lista.append(dto)
        return lista

