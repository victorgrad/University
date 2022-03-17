class Eroare(Exception):
    """
    clasa erorilor
    """
    pass


class Comanda:
    """
    clasa comenzilor
    """
    def __init__(self, id, nume_client, tip_produs, valoare):
        """
        initializam comanda
        id - int
        nume_client - str
        tip_produs - str
        valoare - int
        :param id:
        :param nume_client:
        :param tip_produs:
        :param valoare:
        """
        self.__id = id
        self.__nume_client = nume_client
        self.__tip_produs = tip_produs
        self.__valoare = valoare

    def get_id(self):
        return self.__id

    def get_nume_client(self):
        return self.__nume_client

    def get_tip_produs(self):
        return self.__tip_produs

    def get_valoare(self):
        return self.__valoare

    def __str__(self):
        return str(self.get_id()) + ', ' + self.get_nume_client() + ', ' + self.get_tip_produs() + ', ' + str(self.get_valoare())


class Rata:
    """
    clasa ratei
    """
    def __init__(self, comanda, nr_rate):
        """
        initializam rata
        comanda - de tip clasa Comanda
        nr_rate - int
        :param comanda:
        :param nr_rate:
        """
        self.comanda = comanda
        self.nr_rate = nr_rate

    def get_rata(self):
        return self.comanda.get_valoare()/self.nr_rate

    def get_nume_client(self):
        return self.comanda.get_nume_client()

    def get_tip_produs(self):
        return self.comanda.get_tip_produs()
