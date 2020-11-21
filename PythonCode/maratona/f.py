n = str(input().upper())
n1 = list(n)
pontoJE = pontoJD = partidasjE = partidasjD = 0

for i in (n1):
    #conta os R e S da lista
    if i == "S":
        pontoJE += 1
    if i == "R":
        pontoJD += 1

    if pontoJD == 5 and pontoJE <=3:
        partidasjD +=1
        pontoJE = 0
        pontoJD = 0
    if pontoJE == 5 and pontoJD <= 3:
        partidasjE += 1
        pontoJE = 0
        pontoJD = 0
    if i == 'Q':
        print('{} ({}) - {} ({})'.format(partidasjD,pontoJD,partidasjE,pontoJE))

# Quantidade de partidas ganhas
if partidasjD == 2:
    print('{} (winner) - {}'.format(partidasjE, partidasjD))
if partidasjE == 2:
    print('{} - {} (winner)'.format(partidasjD, partidasjE))
