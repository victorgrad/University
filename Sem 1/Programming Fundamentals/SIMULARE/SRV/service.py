from REPO.repository import *

class Service:
    """
    clasa service/controllerul aplicatiei in spatele caruia se afla logica programului
    """
    def __init__(self, repository):
        """
        initializarea service-ului
        repository - de tipul clasa Repository()
        :param repository:
        """
        self.repository = repository

    def comenzi_cu_str(self, intrare):
        """
        Functia preia stringul intrare, verifica toate comezile si returneaza o lista cu comenzile care contin stringul respectiv la tipul de produs
        intrare - string
        :param intrare:
        :return:
        """
        lista = []
        for comanda in self.repository.comenzi:
            if intrare in self.repository.comenzi[comanda].get_tip_produs():
                lista.append(self.repository.comenzi[comanda])
        return lista

    def rata(self, id_comanda, nr_rate):
        """
        Functia preia id-ul comenzii si nr de rate dorit si returneaza un tuplu cu datele corespunzaotoare
        id_comanda - int
        nr_rate - int
        Ridica Eroare("Comanda inexistenta") cand id-ul comenzii nu se afla in memorie
        :param id_comanda:
        :param nr_rate:
        :return:
        """
        if id_comanda not in self.repository.comenzi:
            raise Eroare("Comanda inexistenta")
        else:
            rata = Rata(self.repository.comenzi[id_comanda], nr_rate)
        return rata.get_nume_client(), rata.get_tip_produs(), rata.get_rata()
