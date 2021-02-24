sexo_m = sexo_f = res_sim = res_nao = 0
qtde = int(input('Digite a quantidade de pessoas entrevistadas: \n'))
for i in range(qtde):
    sexo = (input('M - masculino ou F - feminino\n'))
    res = int(input('1 para SIM ou 0 para NÃO\n'))

    if res == 1:
        res_sim += 1
    if res == 0:
        res_nao += 1
    if sexo.upper() == 'M':
        sexo_m +=1
    if sexo.upper() == 'F':
        sexo_f += 1

porc_f = ((sexo_f * 100)/qtde)
porc_m = ((sexo_m * 100)/qtde)


print('Quantidade de respostas positivas: ',res_sim)
print('Quantidade de respostas negativas: ',res_nao)
print('Quantidade de respostas do sexo masculino: ',sexo_m)
print('Quantidade de respostas do sexo feminino: ',sexo_f)
print('Porcentagem de pessoas do sexo feminino {:.0f}%'.format(porc_f))
print('Porcentagem de pessoas do sexo masculino {:.0f}%'.format(porc_m))