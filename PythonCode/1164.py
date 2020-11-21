#QUESTÃO: NUMERO PERFEITO
n = int(input())
for i in range(n):
    nun = int(input())
    total = 0
    for c in range(1, nun):
        if nun % c == 0:
            total += c
    if total == nun:
        print('{} eh perfeito'.format(nun))
    else:
        print('{} nao eh perfeito'.format(nun))