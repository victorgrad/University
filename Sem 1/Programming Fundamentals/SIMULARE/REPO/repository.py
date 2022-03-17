from DOM.domeniu import *

class Repository:
    """
    clasa repository-ului
    """
    def __init__(self):
        """
        initializam repository-ul
        """
        self.comenzi = {}
        lista = self.loadFromFile()
        for elem in range(0, len(lista)):
            self.comenzi[lista[elem].get_id()] = lista[elem]

    def loadFromFile(self):
        """
        Preia toate comenzile dintr-un fisier si returneaza o lista cu elemente de tip clasa Comanda
        Daca nu reuseste sa preia date din fisier acesta returneaza o lista goala
        :return:
        """
        try:
            f = open("comenzi.txt", "r")
        except IOError:
            return []
        rez = []
        line = f.readline().strip()
        while line != '':
            cmd = line.split(', ')
            comanda = Comanda(int(cmd[0]), cmd[1], cmd[2], int(cmd[3]))
            rez.append(comanda)
            line = f.readline().strip()
        f.close()
        return rez