def prim(n):
    div=0
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            div = div + 1
    if div <= 0:
        return 1
    else:
        return 0
        

nr=int(input('Introduceti numarul: '))
if nr<=1:
    print("Primul numar prim mai mare decat ", nr, " este 2")
else:
    n=nr+1
    while 1:
        if(prim(n)):
            print("Primul numar prim mai mare decat ", nr, " este ", n)
            break
        n=n+1
