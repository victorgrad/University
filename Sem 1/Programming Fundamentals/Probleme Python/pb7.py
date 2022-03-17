n=int(input("Introduceti n: ")) #intreaba despre int
p=0
if n < 0:
    print("introduceti un numar natural")
else:
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            if p==0: # daca nr nu este prim se intra 
                p+=1
            p = p*i
print("Produsul este ",p)
