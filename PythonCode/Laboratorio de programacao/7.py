import random

def Ler_vetor():
    funcionarios = 50
    return random.sample(range(100), funcionarios)

def Somar(v):
    soma = sum(v)
    return soma

def Maior(v):
    return max(v)

def Menor(v):
    return min(v)

def Media(v):
    return (sum(v)/len(v))


vetor = Ler_vetor()

print("Salarios: {}".format(vetor))

print('Valor da folha salarial da empresa: {} R$'.format(Somar(vetor)))

print('Valor do maior salário: {} R$'.format(Maior(vetor)))

print('Valor do menor salário: {} R$'.format(Menor(vetor)))

print('Valor da Média dos salários: {:.0f}'.format(Media(vetor)))
