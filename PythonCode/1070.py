#Questão: Seis Números Ímpares
x = int(input())
if (x % 2 == 0):
    x += 1
    for i in range(x,x + 12,2):
        print(i)
else:
    for i in range(x,x + 12, 2):
        print(i)