valor = float(input())
valor += 0.001
n100 = valor / 100.00
r100 = valor % 100.00

n50 = r100 / 50.00
r50 = r100 % 50.00

n20 = r50 / 20.00
r20 = r50 % 20.00

n10 = r20 / 10.00
r10 = r20 % 10.00

n5 = r10 / 5.00
r5 = r10 % 5.00

n2 = r5 / 2.00
r2 = r5 % 2.00

n1 = r2 / 1.00
r1 = r2 % 1.00

c50 = r1 / 0.50
rc50 = r1 % 0.50

c25 = rc50 / 0.25
rc25 = rc50 % 0.25

c10 = rc25 / 0.10
rc10 = rc25 % 0.10

c5 = rc10 / 0.05
rc5 = rc10 % 0.05

c1 = rc5 / 0.01
cr1 = rc5 % 0.01

print("NOTAS:")
print("%i nota(s) de R$ 100.00"%n100)
print("%i nota(s) de R$ 50.00"%n50)
print("%i nota(s) de R$ 20.00"%n20)
print("%i nota(s) de R$ 10.00"%n10)
print("%i nota(s) de R$ 5.00"%n5)
print("%i nota(s) de R$ 2.00"%n2)
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00"%n1)
print("%i moeda(s) de R$ 0.50"%c50)
print("%i moeda(s) de R$ 0.25"%c25)
print("%i moeda(s) de R$ 0.10"%c10)
print("%i moeda(s) de R$ 0.05"%c5)
print("%i moeda(s) de R$ 0.01"%c1)