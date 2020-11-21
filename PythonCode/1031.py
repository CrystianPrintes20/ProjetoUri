def retante():
    k = 0
    r = 0
    for i in range(n):
        r = (r + k) % i
    return r
if __name__ == '__main__':
    n = x = y = j = num = pulo = 0
    while True:
        n = int(input())
        if (n == 0):
            break
        y = 1
        if(retante(n, y) !=11):
            y += 1
        else:
            break
        print(y)