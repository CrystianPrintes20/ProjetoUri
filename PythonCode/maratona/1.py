#Eleição
#by: Crystian Printes
n = int(input('Numero de habitantes:\n'))
lista_votos = []
indice = []
ganhador = " "
for i in range(n):
    voto = int(input('Digite 1 para votar no candidato A, 2 para o candidato B e 3 para o candidato C\n'))
    lista_votos.append(voto)
    a = lista_votos.count(1)
    b = lista_votos.count(2)
    c = lista_votos.count(3)
    if voto == 2:
        indice.append(i)
    if (a == b and a > c) or (a == c and c > b) or (b == c and b > a):
        ganhador = "Nao houve vencedor!"
    else:
        if a > b and a > c:
            ganhador = "Canditado A venceu"
        if b > a and b > c :
            ganhador = "Canditado B venceu"
        if c > a and c > b:
            ganhador = "Canditado C venceu"

print('O candidato A teve {} votos.'.format(a))
print('O candidato B teve {} votos.'.format(b))
print('O candidato C teve {} votos.'.format(c))
print("Posição de cada voto do canditado B: {}".format(indice))
print("Resultado: {}".format(ganhador))