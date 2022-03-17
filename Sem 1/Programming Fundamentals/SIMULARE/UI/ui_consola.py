from SRV.service import *

def run(consola):
    """
    Ruleaza consola
    consola - de tip clasa Consola
    :param consola:
    :return:
    """
    meniu = "1. Căutarea de comenzi pe baza tipului de produse.\n2. Calcularea de rate."
    while True:
        print(meniu)
        comanda = input()
        if comanda == '1':
            consola.afis_comenzi()
        elif comanda == '2':
            consola.afis_rate()
        else:
            print("Comanda introdusa nu este valida!")


class Consola:
    """
    clasa consolei
    """
    def __init__(self, service):
        """
        initializarea consolei
        service - de tipul clasa Service()
        :param service:
        """
        self.service = service

    def afis_comenzi(self):
        """
        Afiseaza comezile de tipul preluat de la tastatura
        :return:
        """
        intrare = input("Introduceti tipul comezii sau o parte din aceasta: ")
        try:
            lista = self.service.comenzi_cu_str(intrare)
            if len(lista) == 0:
                raise Eroare("Nu au fost gasite comenzi")
            for elem in range(0, len(lista)):
                print(lista[elem])
        except Eroare as ex:
            print(ex)

    def afis_rate(self):
        """
        Preia id-ul comenzii si numarul de rate dorit si afiseaza numele clientului, tipul de produse și valoarea unei singure rate.
        :return:
        """
        id_comanda = input("Introduceti id-ul comenzii: ")
        try:
            id_comanda = int(id_comanda)
        except ValueError:
            print("Nu ati introdus un id valid")
        nr_rate = input("Introduceti numarul de rate dorit: ")
        try:
            nr_rate = int(nr_rate)
            if nr_rate <= 0:
                print("Numarul de rate trebuie sa fie >=0")
            else:
                try:
                    comanda = self.service.rata(id_comanda, nr_rate)
                    print(comanda[0] + ', ' + comanda[1] + ', ' + str(comanda[2]))
                except Eroare as ex:
                    print(ex)
        except ValueError:
            print("Nu ati introdus un nr de rate valid")
