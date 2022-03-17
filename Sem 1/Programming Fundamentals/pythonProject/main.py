import os
import cmath

def get_real(a):
    return a.real

def get_imag(a):
    return a.imag

def set_real(a,b):
    """
    Seteaza partea reala a numarului complex a la b
    :param a:
    :param b:
    :return z:
    """
    c=a.imag
    z=complex(b,c)
    return z

def set_imag(a,b):
    """
    Seteaza partea imaginara a numarului complex a la b
    :param a:
    :param b:
    :return z:
    """
    c=a.real
    z=complex(c,b)
    return z

def clear():
    """
    Functia clear are rolul de a curata consola
    """
    os.system('cls')


def prim(n):
    """
    Functia prim are rolul de a indica daca numarul n primit ca parametru este prim sau nu, returnand valoarea de adevar
    :param n:
    :return:
    """
    if n <= 1:
        return False
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True


def afisare(lista):
    """
    Functia afisare afiseaza lista din parametrii
    :param lista:
    """
    print(lista)


def modul(z):
    """
    Functia modul calculeaza si returneaza modulul numarului complex z
    :param z:
    :return m:
    """
    m = get_real(cmath.sqrt(get_imag(z) ** 2 + get_real(z) ** 2))
    return m


def add_nr():
    """
    Functia add_nr citeste partea reala si imaginara a numarului pe care dorim sa il adaugam si returneaza partea reala(a) si partea imaginara(b) a numarului
    :return a,b:
    """
    try:
        a = int(input("Introduceti partea reala a numarului: "))
        b = int(input("Introduceti partea imaginara a numarului: "))
        return a, b
    except:
        print("Nu ati introdus numere corespunzatoare")
        add_nr()


def ins_nr(lista):
    """
    Fucntia ins_nr preia partea reala si imaginara a unui numar complex pe care dorim sa il adaugam si il insereaza pe pozitia dorita
    :param lista:
    :returneaza lista modificata prin referinta:
    """
    try:
        z = add_nr()
        c = int(input("Introduceti pozitia in care doriti sa inserati numarul(indexarea e de la 0): "))
        lista.insert(c, complex(z[0], z[1]))
    except:
        print("Nu ati introdus o pozitie valida")
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


def tiparire_imag(lista):
    """
    Functia tiparire_imag tipareste partea imaginara pentru numerele din lista dintr-un anumit interval citit
    :param lista:
    :return:
    """
    interval = input("Introduceti intervalul dorit separat printr-un spatiu: ")
    rez = []
    try:
        interval = [int(i) for i in interval.split(' ')]
        if interval[0] <= interval[1]:
            for i in range(interval[0], interval[1]+1):
                rez.append( get_imag(lista[i]) )
            print(rez)
        else:
            print("Nu ati introdus un interval corespunzator")
    except:
        print("Nu ati introdus un interval corespunzator")


def tiparire_lsten(lista):
    """
    Fucntia tiparire_lsten tipareste toate numerele complexe din lista care au modulul mai mic decat 10
    :param lista:
    :return:
    """
    rez = []
    for i in range(0,len(lista)):
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


def ui_adaugare_nr(lista):
    """
    Functia ui_adaugare_nr face legatura intre meniul principal si functiile de adaugare a numerelor complexe in lista printr-un alt meniu ajutator
    :param lista:
    """
    # clear()
    print("1. Adauga un numar complex la sfarsitul listei\n2. Inserare numar complex pe o pozitie data")
    try:
        optiune = int(input("Introduceti optiunea: "))
        if optiune == 1:
            z = add_nr()
            lista.append(complex(z[0], z[1]))
        elif optiune == 2:
            ins_nr(lista)
        else:
            print("Nu ati introdus o optiune valida\n")
    except:
        print("Nu ati introdus o optiune valida\n")


def ui_modificare_el(lista):
    """
    Functia ui_modificare_el face legatura intre meniul principal si functiile de modificare a listei prin intermediul unui alt meniu ajutator
    :param lista:
    :return:
    """
    print("1. Sterge elemente din lista\n2. Inlocuieste elemente din lista")
    try:
        optiune = int(input("Introduceti optiunea: "))
        if optiune == 1:
            interval = input(
                "Introduceti indexul elementului pe care doriti sa il stergeti sau intervalul de indexi separati printr-un spatiu: ")
            try:
                interval = [int(i) for i in interval.split(' ')]
                lista = sterge_el(lista, interval[0], interval[1])
            except:
                print("Nu ati introdus un numar sau un interval bun")
        elif optiune == 2:
            print("Introduceti numarul complex pe care doriti sa il inlocuiti")
            z = add_nr()
            x = complex(z[0], z[1])
            print("Introduceti numarul complex cu care doriti sa inlocuiti numarul complex introdus anterior")
            z = add_nr()
            y = complex(z[0], z[1])
            lista=inlocuire_el(lista,x,y)
        else:
            print("Nu ati introdus o optiune valida\n")
    except:
        print("Nu ati introdus o optiune valida\n")


def ui_cautare(lista):
    """
    Functia ui_cautare face legatura intre meniul principal si functiile de afisare cu cerintele corespunzatoare cautarii
    :param lista:
    :return:
    """
    print("1. Tipareste partea imaginara pentru numerele dintr-un interval\n2. Tipareste toate numerele complexe care au modulul mai mic decat 10\n3. Tipareste toate numerele complexe care au modulul egal cu 10")
    try:
        optiune = int(input("Introduceti optiunea: "))
        if optiune == 1:
            tiparire_imag(lista)
        elif optiune == 2:
            tiparire_lsten(lista)
        elif optiune == 3:
            tiparire_eqten(lista)
        else:
            print("Nu ati introdus o optiune valida\n")
    except:
        print("Nu ati introdus o optiune valida\n")


def ui_filtrare(lista):
    """
    Functia ui_filtrare face legatura intre meniu principal si functiile de afisare cu cerintele corespunzatoare filtrarii
    :param lista:
    :return:
    """
    print("1.Elimina din lista numerele complexe care au partea reala numar prim\n2.Elimina din lista numerele complexe care au modulul mai mic,mai mare sau egal cu un numar dat")
    try:
        optiune = int(input("Introduceti optiunea: "))
        if optiune == 1:
            afisare(elimin_prim(lista))
        elif optiune == 2:
            pass
        else:
            print("Nu ati introdus o optiune valida\n")
    except:
        print("Nu ati introdus o optiune valida\n")


def test_elimin_prim():
    """
    Functia test_elimin_prim testeaza functia elimin_prim din cadrul filtrarii
    :return:
    """
    assert elimin_prim([(1 + 3j), (2 + 4j), (3 + 5j), (6 + 6j), (4 + 3j), (7 + 13j)]) == [(1 + 3j), (6 + 6j), (4 + 3j)]
    assert elimin_prim([(2 + 5j), (2 + 3j), (2 + 1j), (2 + 7j), (2 + 8j), (2 + 9j)]) == []
    assert elimin_prim([(6 + 5j), (6 + 3j), (6 + 1j), (6 + 7j), (6 + 8j), (6 + 9j)]) == [(6 + 5j), (6 + 3j), (6 + 1j), (6 + 7j), (6 + 8j), (6 + 9j)]


def test_sterge_el():
    """
    Functia test_sterge_el testeaza functia sterge_el din cadrul modificarii listei
    :return:
    """
    assert sterge_el([(1 + 3j), (2 + 4j), (3 + 5j), (6 + 6j), (4 + 3j), (7 + 13j)], 1 , 2) == [(1 + 3j), (6 + 6j), (4 + 3j), (7 + 13j)]
    assert sterge_el([(1 + 3j), (2 + 4j), (3 + 5j), (6 + 6j), (4 + 3j), (7 + 13j)], 0 , 5) == []
    assert sterge_el([(1 + 3j), (2 + 4j), (3 + 5j), (6 + 6j), (4 + 3j), (7 + 13j)], 1, 5) == [(1 + 3j)]


def test_inlocuire_el():
    """
    Functia test_inlocuire_el testeaza functia inlocuire_el din cadrul modificarii listei
    :return:
    """
    assert inlocuire_el([(1 + 3j), (2 + 4j), (3 + 5j), (6 + 6j), (1 + 3j), (7 + 13j)], (1 + 3j), (6 + 9j)) == [(6 + 9j), (2 + 4j), (3 + 5j), (6 + 6j), (6 + 9j), (7 + 13j)]
    assert inlocuire_el([(1 + 3j), (2 + 4j), (3 + 5j), (6 + 6j), (1 + 3j), (7 + 13j)], (1 + 1j), (0 + 0j)) == [(1 + 3j), (2 + 4j), (3 + 5j), (6 + 6j), (1 + 3j), (7 + 13j)]
    assert inlocuire_el([(1 + 3j), (2 + 4j), (3 + 5j), (6 + 6j), (1 + 3j), (7 + 13j)], (7 + 13j), 4j) == [(1 + 3j), (2 + 4j), (3 + 5j), (6 + 6j), (1 + 3j), 4j]


def run_tests():
    """
    Fucntia run_tests ruleaza toate testele
    :return:
    """
    test_elimin_prim()
    test_sterge_el()
    test_inlocuire_el()


def main():
    """
    Corpul principal al programului
    :return:
    """
    lista = []
    while True:
        # clear()
        menu_str = "P1: NUMERE\n1. Adauga un numar complex in lista\n2. Modifica elementele din lista curenta\n3. Cauta numere in lista cu anumite proprietati\n4. Filtreaza elementele listei\n5. Afisare sir curent\n6. Iesire din program"
        print(menu_str)
        try:
            optiune = int(input("Introduceti optiunea: "))
            if optiune == 1:
                ui_adaugare_nr(lista)
            elif optiune == 2:
                ui_modificare_el(lista)
            elif optiune == 3:
                ui_cautare(lista)
            elif optiune == 4:
                ui_filtrare(lista)
            elif optiune == 5:
                afisare(lista)
            elif optiune == 6:
                break
            else:
                print("Nu ati introdus o optiune valida\n")
        except:
            print("Nu ati introdus o optiune valida\n")

run_tests()
main()