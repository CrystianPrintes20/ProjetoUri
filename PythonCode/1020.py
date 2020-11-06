N = int(input())
ano = N // 365
r_ano = N % 365
mes = r_ano // 30
r_mes = r_ano % 30
dia = r_mes
print(ano,"ano(s)")
print(mes,"mes(es)")
print(dia,"dia(s)")