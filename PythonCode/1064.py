a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

valor =  []

if a > 0:
    valor += [a]
if b > 0:
    valor += [b]
if c > 0:
    valor += [c]
if d > 0:
    valor += [d]
if e > 0:
    valor += [e]
if f > 0:
    valor += [f]
qtde_vetor = len(valor)
soma = sum(valor)
resultado = soma / qtde_vetor
print('{} valores positivos'.format(qtde_vetor))
print('{:.1f}'.format(resultado))