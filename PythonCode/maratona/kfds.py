n, a, b = input().split()
n = int(n)
a = int(a)
b = int(b)
lista = []
for i in range(a, b+1):
    lista += [i]
    qtde = len(lista)
resul = n/qtde
print(resul)
"""resul *= 3
print('{:.5f}'.format(resul))"""