cod,qtde = input().split()
cod = int(cod)
qtde = int(qtde)
if cod == 1:
    valor = 4 * qtde
elif cod == 2:
    valor = 4.5 * qtde
elif cod == 3:
    valor = 5 * qtde
elif cod == 4:
    valor = 2 * qtde
elif cod == 5:
    valor = 1.5 * qtde
print("Total: R$ %.2f" %valor)