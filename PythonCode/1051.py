#Questão: Imposto de renda
a = float(input())
if (a > 0.00) and (a <= 2000.00):
    print('Isento')
elif (a > 2000.00) and (a <= 3000.00):
    taxa = (a - 2000.00)
    total = ((taxa * 8)/100)
    print('R$ {:.2f}'.format(total))
elif (a > 3000.00) and (a <= 4500.00):
    taxa = (a - 2000.00)
    total1 = (taxa -1000.00)
    taxa2 = ((1000.00 * 8)/100)
    taxa3 = ((total1 * 18)/100)
    total = taxa3 + taxa2
    print('R$ {:.2f}'.format(total))
elif (a > 4500.00):
    #taxa = (a - 2000.00)
    #total1 = (taxa - 1000.00)

    taxa2 = ((1000.00 * 8)/100)
    #total2 = (total1 - 1500.00)
    
    taxa3 = ((1500.00 * 18)/100)
    taxa4 = ((total2 * 28)/100)

    total = taxa4+taxa3+taxa2
    print('R$ {:.2f}'.format(total))