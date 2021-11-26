#Questão: Aumento de Sálario
a = float(input())
if a <= 400:
    rg = ((a * 15)/100)
    ns = a + rg
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 15 %')
elif (a > 400) and (a <= 800):
    rg = ((a * 12) / 100)
    ns = a + rg
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 12 %')
elif (a > 800) and (a <= 1200):
    rg = ((a * 10) / 100)
    ns = a + rg
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 10 %')
elif (a > 1200) and (a <= 2000):
    rg = ((a * 7) / 100)
    ns = a + rg
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 7 %')
elif(a > 2000):
    rg = ((a * 4) / 100)
    ns = a + rg
    print('Novo salario: {:.2f}'.format(ns))
    print('Reajuste ganho: {:.2f}'.format(rg))
    print('Em percentual: 4 %')