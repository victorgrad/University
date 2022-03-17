menu_str = "1.Introduceti lista de numere\n2.Gasiti secventa in care oricare doua elemente consecutive difera printr-un numar prim\n3.Gasiti secventa cu suma maxima\n4.Gasiti secventa cu suma egala cu 5\n5.Iesiti din program"
lista = []
import os
def clear():
    os.system('cls')

def citire():
    global lista
    lista = input("Introduceti numerele separate printr-un spatiu: ")
    lista = [int(i) for i in lista.split(' ')]

def prim(n):
    if n <= 1:
        return False
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True

def prob1():
    inc = -1
    sf = -1
    incm = 0
    sfm = 0
    for i in range(1,len(lista)):
        d=0
        if lista[i]>lista[i-1]:
            d=lista[i]-lista[i-1]
        else:
            d=lista[i-1]-lista[i]
        if prim(d):
            if inc != -1:
                sf=i
            else:
                inc = i-1
                sf = i
        else:
            if sf-inc>sfm-incm and inc != -1:
                sfm=sf
                incm=inc
            inc = -1
            sf = -1
    if (sf-inc)>(sfm-incm) and inc != -1:
        sfm=sf
        incm=inc
    print(lista[incm:sfm+1])

def prob2():
    sm=-999900000
    sc=0
    inc=-1
    sf=-1
    incm=-1
    sfm=-1
    for i in range(0,len(lista)):
        if sc+lista[i]>=lista[i]:
            if inc==-1:
                inc = i
                sf = i
            else:
                sf = i
            sc=sc+lista[i]
            if sc>sm:
                sm=sc
                incm=inc
                sfm=sf
            elif sc==sm: # daca sumele sunt egale verificam lungimile sa fie si lungimea maxima
                if sf-inc+1<sfm-incm+1:
                    incm=inc
                    sfm=sf
        else: #aici se intra daca elementul e mai mare decat suma pana la el cu tot cu el si se reseteaza secv
            sc=lista[i]
            inc=i
            sf=i
    if sc>sm:
        sm=sc
        incm=inc
        sfm=sf
    elif sc==sm: # daca sumele sunt egale verificam lungimile sa fie si lungimea maxima
        if sf-inc+1<sfm-incm+1:
            incm=inc
            sfm=sf
    print(lista[incm:sfm+1])

def prob3():
    #2 3 1 1 1 2 1 1 1 1 1
    sc=0 
    incm=-1
    sfm=-1
    for i in range(0,len(lista)):
        sc=0
        for j in range(i,len(lista)):
            sc+=lista[j]
            if sc==5 and j-i>sfm-incm:
                sfm=j
                incm=i
    if incm==-1:
        print("Nu s-a gasit o secventa cu suma 5")
    else:
        print(lista[incm:sfm+1])
    
while True:
    clear()
    print(menu_str)
    optiune = int(input("Introduceti Optiunea: "))
    if optiune == 5:
        break
    elif optiune == 1:
        citire()
    elif optiune == 2:
        prob1()
    elif optiune == 3:
        prob2()
    elif optiune == 4:
        prob3()
    else:
        print("Comanda nu exista")
        print("")
