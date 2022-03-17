print('Suma a n numere')
n = int(input('Cate numere citim(n): '))
s = 0
if n <= 0:
    print('Suma este 0')
else:
    for i in range(0, n):
        nr = int(input())
        s = s+nr
    print('Suma este ', s)
