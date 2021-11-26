#Questão: Triângulo
a,b,c = map(float, input().split())

if (a+b)>c and (b+c)>a and (c+a)>b:
    P = a+ b+c
    print("Perimetro =",P)
else:
    A = (((a + b) * c)/2)
    print("Area =",A)