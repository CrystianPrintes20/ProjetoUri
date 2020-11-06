x = []
for i in range(1, 101):
    x.append(int(input()))
    maior = max(x)
    posicao = x.index(maior)
print(maior)
print(posicao+1)