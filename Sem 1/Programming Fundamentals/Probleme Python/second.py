print('Verificarea daca numarul este prim')
nr = int(input('Introdu nuamrul: '))
div = 0
if nr<2:
    print('nu e prim')
else:
    for i in range(2, int(nr/2)+1):
        if nr%i == 0:
            div = div + 1
    if div > 0:
        print('nu e prim')
    else:
        print('prim')
        
