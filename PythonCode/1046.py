#Questão: Tempo de jogo
a,b = map(int, input().split())
if a == b:
    print("O JOGO DUROU 24 HORA(S)")
elif b > a:
    x = abs(a - b)
    print("O JOGO DUROU",x,"HORA(S)")
elif b < a:
    x = (abs(a-24)+b)
    print("O JOGO DUROU",x,"HORA(S)")