#Nomes e idade
# by: Crystian Printes
n = int(input('Numero de pessoas particpantes: '))
pessoas = []
for c in range(n):
    nome, idade = map(str, input('Digite o NOME, dê um espaço e em seguida digite a IDADE da pessoa\n').split())
    pessoas += [[nome, int(idade)]]
    ordenado = sorted(pessoas, key=lambda pessoas: pessoas[1])

print('Nome e idade de todas as pessoas participantes em ordem crescente:\n',ordenado)