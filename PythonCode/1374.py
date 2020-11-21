#QUESTÃO: ELETRICIDADE
while True:
    try:
        n_dias = 0
        consumo = 0
        l = []
        l1 = []
        l_aux = []
        v1 = []
        v2 = []
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            d, m, y, c = map(int, input().split())
            l = [d, m, y, c]
            l_aux = l1
            l1 = l
            if len(l_aux) != 0:

                t = [4, 6, 9, 11]
                t1 = [1, 3, 5, 7, 8, 10, 12]
                # verifica se os anos, meses são iguais e os dias consecutivos
                if l_aux[2] == l[2] and l_aux[1] == l[1] and l_aux[0] + 1 == l[0]:
                    n_dias += 1
                    consumo += l[3] - l_aux[3]
                    v1 += [n_dias]
                    v2 += [consumo]
                else:
                    v1 += [0]
                    v2 += [0]

                if l_aux[1] in t:
                    # verifica se os anos são iguais e se os meses com final 30 e os dias consecutivos
                    if l_aux[2] == l[2] and l_aux[1] + 1 == l[1] and l_aux[0] == 30 and l[0] == 1:
                        n_dias += 1
                        consumo += l[3] - l_aux[3]
                        v1 += [n_dias]
                        v2 += [consumo]
                    else:
                        v1 += [0]
                        v2 += [0]

                if l_aux[1] in t1:
                    # verifica se os anos são iguais e se os meses com final 31 e os dias consecutivos
                    if l_aux[2] == l[2] and l_aux[1] + 1 == l[1] and l_aux[0] == 31 and l[0] == 1:
                        n_dias += 1
                        consumo += l[3] - l_aux[3]
                        v1 += [n_dias]
                        v2 += [consumo]
                    else:
                        v1 += [0]
                        v2 += [0]

                # verifica ano novo
                if l_aux[2] + 1 == l[2] and l_aux[1] == 12 and l[1] == 1 and l_aux[0] == 31 and l[0] == 1:
                    n_dias += 1
                    consumo += l[3] - l_aux[3]
                    v1 += [n_dias]
                    v2 += [consumo]
                else:
                    v1 += [0]
                    v2 += [0]

                    # verifica se os anos são iguais e se os mese de fervereiro termina com 28 ou 29 e os dias consecutivos
                if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
                    if l_aux[2] == l[2] and l_aux[1] == 2 and l[1] == 3 and l_aux[0] == 29 and l[0] == 1:
                        n_dias += 1
                        consumo += l[3] - l_aux[3]
                        v1 += [n_dias]
                        v2 += [consumo]
                    else:
                        v1 += [0]
                        v2 += [0]

                else:
                    if l_aux[2] == l[2] and l_aux[1] == 2 and l[1] == 3 and l_aux[0] == 28 and l[0] == 1:
                        n_dias += 1
                        consumo += l[3] - l_aux[3]
                        v1 += [n_dias]
                        v2 += [consumo]
                    else:
                        v1 += [0]
                        v2 += [0]

        print('{} {}'.format(max(v1), max(v2)))
    except EOFError:
        break