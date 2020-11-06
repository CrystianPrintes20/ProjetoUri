tentativas = int(input())
quebrados = 0

for i in range(tentativas):
    l, c = input().split()
    if int(l) > int(c):
        quebrados += int(c)
print(quebrados)