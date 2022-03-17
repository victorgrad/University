import os
from user_interface import *
from teste import *


def clear():
    """
    Functia clear are rolul de a curata consola
    """
    os.system('cls')


def meniu_nou(lista):
    """
    Meniul care preia comenzile una dupa alta sub forma de sir
    :return:
    """
    print("Comenzile posibile sunt:\nadaugare a b (adauga numarul complex a+bj la finalul listei)\nsterge x (sterge numarul complex de pe pozitia x)\nsuma a b (afiseaza suma numerelor complexe din intervalul [a,b])\n"
          "undo (reface ultima modificare asupra sirului)\nafisare (afiseaza sirul curent)")
    lista_comenzi = input("Dati o lista de comenzi separate prin virgula, iar parametrii separati de comanda si intre ei printr-un spatiu:\n")
    lista_comenzi = lista_comenzi.split(',')
    for comanda in lista_comenzi:
        comanda = comanda.split(' ')
        if comanda[0] == "adaugare":
            try:
                add_lista(lista, int(comanda[1]), int(comanda[2]))
            except ValueError:
                print("Nu s-a adaugat nr complex ", comanda[1], "+ (", comanda[2], "j )")
        elif comanda[0] == "sterge":
            try:
                lista=sterge_el(lista, int(comanda[1]), int(comanda[1]))
                lista_h.append(copie(lista))
            except IndexError:
                print("Nu s-a sters nr complex de pe pozitia", comanda[1])
            except ValueError:
                print("Nu ati introdus o pozitie valida")
        elif comanda[0] == "suma":
            try:
                print(suma_sub(lista, int(comanda[1]), int(comanda[2])))
            except:
                print("Nu s-a afisat suma numerelor din interval")
        elif comanda[0] == "undo":
            lista = copie(undo())
        elif comanda[0] == "afisare":
            afisare(lista)
        else:
            print("Nu s-a efectuat", comanda[0])
    return lista

def main():
    """
    Corpul principal al programului
    :return:
    """
    lista = []
    while True:
        # clear()
        menu_str = "P1: NUMERE\n1. Adauga un numar complex in lista\n2. Modifica elementele din lista curenta\n3. Cauta numere in lista cu anumite proprietati\n4. Operatii cu numere complexe din lista\n5. Filtreaza elementele listei\n6. Afisare sir curent\n7. Undo\n8. Meniu nou\n9. Iesire din program"
        print(menu_str)
        try:
            optiune = int(input("Introduceti optiunea: "))
            if optiune == 1:
                ui_adaugare_nr(lista)
            elif optiune == 2:
                ui_modificare_el(lista)
            elif optiune == 3:
                ui_cautare(lista)
            elif optiune ==4:
                ui_operatii(lista)
            elif optiune == 5:
                ui_filtrare(lista)
            elif optiune == 6:
                afisare(lista)
            elif optiune == 7:
                lista = copie(undo())
            elif optiune == 8:
                lista = meniu_nou(lista)
            elif optiune == 9:
                print("by!!!")
                break
            else:
                print("Nu ati introdus o optiune valida\n")
        except:
            print("Nu ati introdus o optiune valida\n")


run_tests()


main()
