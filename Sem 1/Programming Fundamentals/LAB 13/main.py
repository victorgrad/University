ok = False

def solutionFound(lista):
    global ok
    ok = True
    print(lista)


def consistent(lista, m, n):
    """
    verifica consistenta listei, adica daca elementele consecutive au diferenta absoluta m si elementele nu se repeta
    lista - list
    m - int
    n - int
    :param lista:
    :param m:
    :param n:
    :return:
    """
    aparitii = [0]*(n+1)
    aparitii[lista[0]] += 1
    for i in range(0, len(lista)-1):
        aparitii[lista[i+1]] += 1
        if aparitii[lista[i+1]] > 1:
            return False
        if abs(lista[i+1]-lista[i]) != m:
            return False
    return True


def solution(lista):
    """
    returneaza true daca lista reprezinta o solutie, adica daca are mai mult de 1 element
    :param lista:
    :return:
    """
    if len(lista) < 2:
        return False
    return True


def backRec(lista, m, n):
    """
    Se dau două numere naturale m şi n. Genereaza liste formate din numere de la 1 la n cu
    proprietatea că diferenţa (în valoare absolută) între două numere consecutive din listă este
    m. Tipăriţi un mesaj dacă problema nu are soluţie.
    lista - list
    m - int
    n - int
    :param m:
    :param n:
    :return:
    """
    lista.append(1)
    for i in range(1, n+1):
        lista[-1] = i
        if consistent(lista, m, n):
            if solution(lista):
                solutionFound(lista)
            backRec(lista, m, n)
    lista.pop()


def backIter(m, n):
    """
    Se dau două numere naturale m şi n. Genereaza liste formate din numere de la 1 la n cu
    proprietatea că diferenţa (în valoare absolută) între două numere consecutive din listă este
    m. Tipăriţi un mesaj dacă problema nu are soluţie.
    m - int
    n - int
    ok - boolean (pentru a contoriza gasirea unei solutii)
    :param m:
    :param n:
    :return:
    """
    lista = [0]
    while len(lista) > 0:
        chosen = False
        while not chosen and lista[-1] < n:
            lista[-1] = lista[-1]+1
            chosen = consistent(lista, m, n)
        if chosen:
            if solution(lista):
                solutionFound(lista)
            lista.append(0)
        else:
            lista = lista[:-1]


if __name__ == '__main__':
    m = int(input("m="))
    n = int(input("n="))
    ok = False
    lista = []
    backIter(m, n)
    #backRec(lista, m, n)
    if not ok:
        print("Nu a fost gasita nicio solutie")
