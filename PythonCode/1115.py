X=Y=1
while (X != 0) and (Y != 0):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X > 0 and Y > 0:
        print("primeiro")
    if X > 0 and Y < 0:
        print("quarto")
    if X < 0 and Y > 0:
        print("segundo")
    if X < 0 and Y < 0:
        print("terceiro")