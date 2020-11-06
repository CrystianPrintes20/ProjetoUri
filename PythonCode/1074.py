n = int(input())
entradas = []
for cont in range(n):
    entradas.append(int(input()))

for i in range(n):
    if entradas[i] % 2 == 0 and entradas[i] < 0:
        print('EVEN NEGATIVE')
    if entradas[i] % 2 == 0 and entradas[i] > 0:
        print('EVEN POSITIVE')
    if entradas[i] % 2 == 1 and entradas[i] < 0:
        print('ODD NEGATIVE')
    if entradas[i] % 2 == 1 and entradas[i] > 0:
        print('ODD POSITIVE')
    if entradas[i] == 0:
        print('NULL')