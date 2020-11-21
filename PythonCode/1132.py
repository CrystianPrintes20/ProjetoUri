#QUESTÃO: MULTIPLOS DE 13
x = int(input())
y = int(input())
cont = 0
if x <= y:
    a = x
    b = y
else:
    a = y
    b = x
for i in range(a, b+1):
    if (i % 13 != 0):
        cont += i
print(cont)