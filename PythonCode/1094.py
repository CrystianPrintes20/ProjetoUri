x = int(input())
coelho = rato = sapo = 0

for i in range(x):
    x = input().split()
    qtde, tipo, = x
    if tipo == 'C':
        coelho = coelho + int(qtde)
    if tipo == 'R':
        rato = rato + int(qtde)
    if tipo == 'S':
        sapo = sapo + int(qtde)

total = coelho + rato + sapo
pc = (coelho / total) * 100
pr = (rato / total) * 100
ps = (sapo / total) * 100

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelho))
print('Total de ratos: {}'.format(rato))
print('Total de sapos: {}'.format(sapo))
print('Percentual de coelhos: {:.2f} %'.format(pc))
print('Percentual de ratos: {:.2f} %'.format(pr))
print('Percentual de sapos: {:.2f} %'.format(ps))