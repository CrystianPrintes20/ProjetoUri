#Cidades e temperatura
# by: Raiane Coimbra & Crystian Printes

class citytemp:
    def __init__(self, nomecity, temp):
        self.nomecity, self.temp, = nomecity, temp

lista_temp = []
lista_city = []
x = []
n = int(input('Numero de Cidade particpantes: '))
for c in range(n):
    nomecity = input('Digite o nome da Cidade ')
    temp = int(input('Digite agora a temperatura: '))
    y = citytemp(nomecity, temp)
    x.append(y)

    lista_temp += [temp]
    lista_city += [nomecity]
    media = sum(lista_temp) / len(lista_temp)
    y = max(x, key = lambda p: p.temp)

    def mais_proximo(lst):
        proximo = {value: abs(value - 23) for value in lst}
        return min(proximo, key=proximo.get)

cidade = mais_proximo(lista_temp)
indicet = lista_temp.index(cidade)

print(cidade)
print(indicet)
print(f'A cidade {y.nomecity} tem a maior temperatura: {y.temp} graus')
print('A temperatura média das cidades foi de {:.1f} graus'.format(media))
print("A cidade com temperatura mais proxima de 23 graus é: {}".format(lista_city[indicet]))
