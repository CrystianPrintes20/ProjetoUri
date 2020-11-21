#Questão: Teste de Seleção 1
A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
Somacd = C + D
Somaab = A + B
Resto_a = A % 2
if B > C and D > A and Somacd > Somaab and Resto_a == 0 and C >= 0 and D >= 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")