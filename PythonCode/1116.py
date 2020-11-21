#QUESTÃO: DIVIDINDO X POR Y
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if y == 0:
        print('divisao impossivel')
    if y != 0:
        print(x/y)