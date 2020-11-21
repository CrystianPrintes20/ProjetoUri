#QUESTÃO: NUMEROS PRIMOS
n = int(input())
for i in range(n):
    nun = int(input())
    total = 0
    for c in range(1, nun+1):
        if nun % c == 0:
            total += 1
    if total == 2:
        print('{} eh primo'.format(nun))
    else:
        print('{} nao eh primo'.format(nun))