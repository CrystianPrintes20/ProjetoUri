x, y = map(int, input().split())
c = 1
while c < y+1:
    if c > y:
        c -= 1
    print(c, c + 1, c + 2)
    c += 3