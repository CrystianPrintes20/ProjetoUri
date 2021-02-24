
def Ler_vetor():
    entrada = input('salario dos funcionarios: ')
    return [int(n) for n in entrada.split(",") ]

def Somar(v):
    return sum(v)

def Maior(v):
    return max(v)

def Menor(v):
    return min(v)

def Media(v):
    return (sum(v)/len(v))

# 1 - Leia dois vetores de numeros inteiros de 10 posicoes
vetor = Ler_vetor()

# 2 - Imprima os dois vetores lidos
print("Salarios: {}".format(vetor))

print('Valor da folha salarial da empresa: {}'.format(Somar(vetor)))

print('Valor do maior salário: {}'.format(Maior(vetor)))

print('Valor do maior salário: {}'.format(Menor(vetor)))

print('Valor da Média dos salários: {:.0f}'.format(Media(vetor)))
