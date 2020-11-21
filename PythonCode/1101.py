#SEQUÊNCIA DE NÚMEROS E SOMA
while True:
    m, n = input().split()
    m = int(m)
    n = int(n)
    aux = soma = 0
    total = ''
    if (m <= 0) or (n <= 0):
        break
    if m > n:
        aux = m
        m = n
        n = aux
    while(m <= n):
        total += str(m) + ' '
        soma += m
        m += 1
    total += 'Sum=%d'
    print(total %soma)