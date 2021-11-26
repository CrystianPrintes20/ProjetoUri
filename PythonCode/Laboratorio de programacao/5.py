print('DIGITE OS VALORES DO TRIÂNGULO:')
a = int(input())
b = int(input())
c = int(input())

lista = [a,b,c]
lista.sort()
lista.reverse()

if(lista[0]>=(lista[1]+lista[2])):
    print("NAO FORMA TRIANGULO")
else:
    if (lista[0] == lista[1] == lista[2]):
        print("TRIANGULO EQUILATERO")
    if (lista[0] == lista[1] != lista[2]) or (lista[0] == lista[2] != lista[1]) or (lista[1] == lista[2] != lista[0]):
        print("TRIANGULO ISOSCELES")
    if (lista[0] != lista[1] != lista[2]):
        print("TRIANGULO ESCALENO")
