senha = int(input('Jogador 1 digite um valor entre 0 a 100 como senha:\n'))
tentativas = 5
if senha >= 0 and senha  <= 100:

    for i in range(tentativas):
        senha2 = int(input(f'Qual é a senha jogador 2 ? Você tem {tentativas} chances!\n'))
        if senha2 == senha:
            print('Acesso permitido!')
        elif senha2 > senha:
            print('Voce digitou um numero maior que a senha!')
        elif senha2 < senha:
            print('Voce digitou um numero menor que a senha!')
        tentativas -= 1
    print('Tentativas esgotadas!')
else:
    print('Digitos fora do intervalo permitido!')