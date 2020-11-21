#QUESTÃO: VÁRIAS NOTAS COM VALIDAÇÃO
total = 0
cont = 0
continuar = True

while continuar == True:
    nota = float(input())

    if nota >= 0.0 and nota <= 10:
        total += nota
        cont += 1

        if cont == 2:

            print("media = %.2f" % (total / 2))
            cont = 0
            total = 0

            while True:
                print("novo calculo (1-sim 2-nao)")
                resp = int(input())
                if resp == 2:
                    continuar = False
                    break
                elif resp == 1:
                    continuar = True
                    break

    else:
        print("nota invalida")