a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

qtde = 0

if a > 0:
    qtde += 1
if b > 0:
    qtde += 1
if c > 0:
    qtde += 1
elif d > 0:
    qtde += 1
if e > 0:
    qtde += 1
if f > 0:
    qtde += 1
print('{} valores positivos'.format(qtde))