import random

while True:
    lin, col = input().split()
    lin = int(lin)
    col = int(col)
    if lin > 0 and col > 0:
        m = []
        for i in range(lin):
            linha = []
            for j in range(col):
                num = random.randint(0, 1)
                linha.append(num)
            m.append(linha)
        break
print(m)