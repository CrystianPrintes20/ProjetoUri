#Multiplicação Vetor
# by: Raiane Coimbra
import numpy
vetor = []
print("Informe o tamanho do vetor:")
tam = int(input())
print("Informe os elementos do vetor:")

for i in range(tam):
    x = int(input())
    vetor.append(x)
r = numpy.prod(vetor)
print("Resultado: {}".format(r))
