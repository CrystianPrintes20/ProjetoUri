grenais = 1
inter = gremio = empates = 0
while True:
    i, g = map(int, input().split())
    print('Novo grenal (1-sim 2-nao)')
    resp = int(input())

    if i > g:
        inter += 1
    elif i < g:
        gremio += 1
    else:
        empates += 1

    if resp == 1:
        grenais += 1
    if resp == 2:
        print('{} grenais'.format(grenais))
        print('Inter:{}'.format(inter))
        print('Gremio:{}'.format(gremio))
        print('Empates:{}'.format(empates))
        if inter > gremio:
            print('Inter venceu mais')
        elif inter == gremio:
            print('Nao houve vencedor')
        else:
            print('Gremio venceu mais')
        break

