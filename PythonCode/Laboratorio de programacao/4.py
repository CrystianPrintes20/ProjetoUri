
'''mat = [[1,31], [2,8], [3,31], [4,30], [5,31], [6,30], [7,31], [8,31], [9,30], [10,31],[11,30], [12,31]]

dt = input('Bem-vindo ao Maredicator!\n Indique a data da última lua cheia e saiba quando haverá lua cheia durante o restante do ano dd/mm/aaaa:\n')

data = dt.split('/')
#14/08/2020 -> 14/09/2020
for mes in range(int(data[1]), 12):
    if(mat[mes-1][1] - int(data[0]) == 30):
        data[0] = mat[mes -1][1] - int(data[0])
        print(int(data[0]),'/',mes,'/', int(data))'''


a = [['carlos', 1234], ['creuza',56], ['antonio',789]]

num = int(input('digite um cpf:'))
for i in range(len(a)):
    for j in range(len(a[i])):
        print(j)
        if [j.in] == num:
            print(a[i][j], end=' ')
        else:
            print('deu errado')
    print()