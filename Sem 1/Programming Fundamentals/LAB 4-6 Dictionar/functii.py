import cmath
from getset import *


lista_h = []


def copie(lista):
    """
    Functia copie cloneaza lista transmisa ca parametru
    :param lista:
    :return:
    """
    copy = lista[:]
    return copy


def prim(n):
    """
    Functia prim are rolul de a indica daca numarul n primit ca parametru este prim sau nu, returnand valoarea de adevar
    :param n:
    :return:
    """
    if n <= 1:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True


def afisare(lista):
    """
    Functia afisare afiseaza lista din parametrii
    :param lista:
    """
    if len(lista) == 0:
        print("Nu exista elemente\n")
    else:
        print(lista)


def modul(z):
    """
    Functia modul calculeaza si returneaza modulul numarului complex z
    :param z:
    :return m:
    """
    m = (cmath.sqrt(get_imag(z) ** 2 + get_real(z) ** 2)).real
    return m


def add_nr():
    """
    Functia add_nr citeste partea reala(a) si imaginara(b) a numarului pe care dorim sa il adaugam si returneaza tuplul (a,b)
    :return a,b:
    """
    try:
        a = int(input("Introduceti partea reala a numarului: "))
        b = int(input("Introduceti partea imaginara a numarului: "))
        return a, b
    except:
        print("Nu ati introdus numere corespunzatoare\n")
        add_nr()


def add_lista(lista, a, b):
    """
    Fucntia add_lista preia partea reala si imaginara a nr complex si il adauga in lista
    :param lista:
    :param a:
    :param b:
    :return:
    """
    complexx = {
        "real": a,
        "imag": b
    }
    lista.append(complexx)
    lista_h.append(copie(lista))


def ins_nr(lista):
    """
    Fucntia ins_nr preia partea reala si imaginara a unui numar complex pe care dorim sa il adaugam si il insereaza pe pozitia dorita
    :param lista:
    :returneaza lista modificata prin referinta:
    """
    try:
        z = add_nr()
        complexx = {
            "real": z[0],
            "imag": z[1]
        }
        c = int(input("Introduceti pozitia in care doriti sa inserati numarul(indexarea e de la 0): "))
        lista.insert(c, complexx)
        lista_h.append(copie(lista))
    except:
        print("Nu ati introdus o pozitie valida\n")
        ins_nr(lista)


def sterge_el(lista,inc,sf):
    """
    Functia sterge_el preia de la tastatura un index sau un interval de indexi si sterge elementele sirului de pe indexii respectivi
    :param lista,inc,sf:
    :return rez:
    """
    rez = lista
    try:
        for i in range(inc, sf + 1):
            rez.pop(inc)
    except:
        rez.pop(inc)
    return rez


def inlocuire_el(lista,x,y):
    """
    Functia inlocuire_el preia de la tastatura un numar complex x si ii inlocuieste toate aparitiile din lista cu numarul complex y
    :param lista:
    :return:
    """
    rez = lista
    for i in range(0, len(lista)):
        if rez[i] == x:
            rez[i] = y
    return rez


def tiparire_imag(lista, inc, sf):
    """
    Functia tiparire_imag tipareste partea imaginara pentru numerele din lista dintr-un anumit interval citit
    :param lista, inc, sf:
    :return:
    """
    rez = []
    try:
        if inc <= sf:
            for i in range(inc, sf+1):
                rez.append(get_imag(lista[i]))
            print(rez)
        else:
            print("Nu ati introdus un interval corespunzator\n")
    except:
        print("Nu ati introdus un interval corespunzator\n")


def tiparire_lsten(lista):
    """
    Fucntia tiparire_lsten tipareste toate numerele complexe din lista care au modulul mai mic decat 10
    :param lista:
    :return:
    """
    rez = []
    for i in range(0, len(lista)):
        if modul(lista[i]) < 10:
            rez.append(lista[i])
    print(rez)


def tiparire_eqten(lista):
    """
    Fucntia tiparire_lsten tipareste toate numerele complexe din lista care au modulul egal cu 10
    :param lista:
    :return:
    """
    rez = []
    for i in range(0,len(lista)):
        if modul(lista[i]) == 10:
            rez.append(lista[i])
    print(rez)


def elimin_prim(lista):
    """
    Functia elimin_prim preia lista "lista" si returneaza lista rezultat rez care contine numerele complexe care nu au partea reala nr prim
    :param lista:
    :return rez:
    """
    rez = []
    for i in range(0,len(lista)):
        if prim(get_real(lista[i])) == False:
            rez.append(lista[i])
    return rez


def comparare(lista,semn,a):
    """
    Functia comparare compara si memoreaza in lista rez, pe care o returneaza, numerele din lista care au modului corespunzator in functie de semnul introdus
    :param lista:
    :param semn:
    :param a:
    :return z:
    """
    rez = []
    if semn == '=':
        for i in range(0,len(lista)):
            if modul(lista[i]) == a:
                rez.append(lista[i])
    elif semn == '<':
        for i in range(0,len(lista)):
            if modul(lista[i]) < a:
                rez.append(lista[i])
    else:
        for i in range(0,len(lista)):
            if modul(lista[i]) > a:
                rez.append(lista[i])
    return rez


def suma_sub(lista,inc,sf):
    """
    Fucntia suma_sub calculeaza suma numerelor din subsecventa data si le returneaza in lista rez
    :param lista:
    :param inc:
    :param sf:
    :return rez:
    """
    rez = {
        "real": 0,
        "imag": 0
    }
    for i in range(inc, sf+1):
        rez["real"] += get_real(lista[i])
        rez["imag"] += get_imag(lista[i])
    return rez


def prod_sub(lista, inc, sf):
    """
    Fucntia suma_sub calculeaza produsul numerelor din subsecventa data si le returneaza in lista rez
    :param lista:
    :param inc:
    :param sf:
    :return rez:
    """
    rez = 1
    for i in range(inc, sf+1):
        rez *= complex(lista[i]["real"], lista[i]["imag"])
    rezz = {
        "real": rez.real,
        "imag": rez.imag
    }
    return rezz


def sortd_lista(lista):
    """
    Fucntia sortd_lista sorteaza descrescator lista dupa imagine si o afiseaza
    :param lista:
    :return rez:
    """
    rez = lista
    rez.sort(reverse=True, key=get_imag)
    return rez


def undo():
    """
    #Functia undo reface ultima operatie asupra listei
    #:param lista:
    #:return rez:
    """
    try:
        lista_h.pop()
        rez = lista_h[len(lista_h) - 1]
        return rez
    except: pass
