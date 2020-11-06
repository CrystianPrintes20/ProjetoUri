A = float(input())
if A >= 0  and A <= 25.0000:
    print("Intervalo [0,25]")
elif A > 25.0000 and A <= 50.0000:
    print("Intervalo (25,50]")
elif A > 50.0000 and A <= 75.0000:
    print("Intervalo (50,75]")
elif A > 75.0000 and A <= 100.0000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")