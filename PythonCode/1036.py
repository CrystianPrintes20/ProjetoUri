#Questão: Formula de bhaskara
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
delta = (B**2) - 4 * A * C
if A != 0 and delta > 0:
    delta1 = delta ** (1 / 2)
    R1 = (-B + delta1) / (2 * A)
    R2 = (-B - delta1) / (2 * A)
    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)
else:
    print("Impossivel calcular")