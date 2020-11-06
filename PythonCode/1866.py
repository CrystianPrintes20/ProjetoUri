n = int(input())
c = []
for i in range(n):
    x = int(input())
    if x % 2 == 1:
        c += [1]
    else:
        c += [0]
for j in c:
    print(j)