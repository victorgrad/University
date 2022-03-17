from functii import *


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
            add_lista(lista, z[0], z[1])
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
                try:
                    lista = sterge_el(lista, interval[0], interval[1])
                except:
                    lista = sterge_el(lista, interval[0], interval[0])
                lista_h.append(copie(lista))
            except:
                print("Nu ati introdus un numar sau un interval bun")
        elif optiune == 2:
            print("Introduceti numarul complex pe care doriti sa il inlocuiti")
            z = add_nr()
            x = {
                "real": z[0],
                "imag": z[1]
            }
            print("Introduceti numarul complex cu care doriti sa inlocuiti numarul complex introdus anterior")
            z = add_nr()
            y = {
                "real": z[0],
                "imag": z[1]
            }
            lista = inlocuire_el(lista, x, y)
            lista_h.append(copie(lista))
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
            interval = input("Introduceti intervalul dorit separat printr-un spatiu: ")
            try:
                interval = [int(i) for i in interval.split(' ')]
                tiparire_imag(lista, interval[0], interval[1])
            except:
                print("Nu ati introdus un interval corespunzator\n")
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
            semn = input("Introduceti semnul comparatiei dorite(<,>,=): ")
            if semn == '<' or semn == '=' or semn == '>':
                try:
                    a = int(input("Introduceti numarul cu care doriti sa comparati: "))
                    z = comparare(lista, semn, a)
                    afisare(z)
                except:
                    print("Nu ati introdus un numar valid\n")
            else:
                print("Nu ati introdus un semn valid\n")
        else:
            print("Nu ati introdus o optiune valida\n")
    except:
        print("Nu ati introdus o optiune valida\n")


def ui_operatii(lista):
    """
    Functia ui_operatii face legatura intre meniu principal si functiile cu operatii pe lista de numere complexe
    :param lista:
    :return:
    """
    print("1. Calculeaza suma numerelor dintr-o subsecventa data\n2. Calculeaza produsul numerelor dintr-o subsecventa data\n3. Tipareste lista sortata descrescator dupa partea imaginara")
    try:
        optiune = int(input("Introduceti optiunea: "))
        if optiune == 1:
            interval = input("Introduceti intervalul de indexi separati printr-un spatiu: ")
            try:
                interval = [int(i) for i in interval.split(' ')]
                print(suma_sub(lista,interval[0],interval[1]))
            except:
                print("Nu ati introdus un numar sau un interval bun\n")
        elif optiune == 2:
            interval = input("Introduceti intervalul de indexi separati printr-un spatiu: ")
            try:
                interval = [int(i) for i in interval.split(' ')]
                print(prod_sub(lista, interval[0], interval[1]))
            except:
                print("Nu ati introdus un numar sau un interval bun\n")
        elif optiune == 3:
            print(sortd_lista(lista))
        else:
            print("Nu ati introdus o optiune valida\n")

    except:
        print("Nu ati introdus o optiune valida\n")