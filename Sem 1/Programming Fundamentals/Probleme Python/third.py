print('CMMDC a doua numere')
n1 = int(input('Introdu primul numar: '))
n2 = int(input('Introdu al doilea numar: '))
if n1>=0 and n2>=0:
    while n1!=n2 and n1>0 and n2>0:
        if n1>n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    if n1==0 or n2==0:
        if n1>n2:
            print(n1)
        elif n2>n1:
            print(n2)
        else:
            print('nedeterminare')
    else:
        print(n1)
else:
    print('Nu ati introdus numere bune')
