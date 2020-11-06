n = int(input())

for i in range(n):
    xy = [int(num) for num in input().split()]
    x = min(xy)
    y = max(xy)
    soma = 0
    for num in range(x+1, y):
        if num%2 !=0:
            soma += num
    print(soma)