x = 0
a = g = d = 0
while x != 4:
    x = int(input())
    if x == 1:
        a = a + 1
    if x == 2:
        g = g + 1
    if x == 3:
        d = d + 1
print('MUITO OBRIGADO')
print('Alcool:',a)
print('Gasolina:',g)
print('Diesel:',d)