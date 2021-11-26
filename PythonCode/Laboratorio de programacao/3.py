jogador1 = str(input('Jogador 1:\n'))
jogador2 = str(input('Jogador 2:\n'))
jogador1, jogador2 = jogador1.upper(), jogador2.upper()

if (jogador1 == 'T' and jogador2 == 'P') or (jogador1 == 'T' and jogador2 == 'L'):
    print('Jogador 1 ganhou.')

elif (jogador1 == 'P' and jogador2 == 'R') or (jogador1 == 'P' and jogador2 == 'S'):
    print('Jogador 1 ganhou.')

elif (jogador1 == 'L' and jogador2 == 'S') or (jogador1 == 'L' and jogador2 == 'P'):
    print('Jogador 1 ganhou.')

elif (jogador1 == 'S' and jogador2 == 'T') or (jogador1 == 'L' and jogador2 == 'R'):
    print('Jogador 1 ganhou.')

else:
    print('Jogador 2 ganhou.')
