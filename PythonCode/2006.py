t = int(input())
entradas = input()
entradas = entradas.split(' ')
cont = 0

for i in range(5):
    if int(entradas[i]) == t:
        cont += 1

print(cont)