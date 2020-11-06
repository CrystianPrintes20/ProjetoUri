n = int(input())
for i in range(n):
    nota01, nota02, nota03 = map(float, input().split())
    total = ((nota01*2) + (nota02*3) + (nota03*5))/10
    print('%.1f' % round(total, 1))