'''W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)'''
#DIA INICAL
dia_i = input().split(' ') #Slip deixa as coisa em vetores
n_dias_i = int(dia_i[1])
#HORA, MINUTOS E SEGUNDOS DO DIA INCIAL
hh_i,mm_i,ss_i = input().split(':')
hh_i = int(hh_i)
mm_i = int(mm_i)
ss_i = int(ss_i)
#DIA FINAL
dia_f = input().split(' ')
n_dias_f = int(dia_f[1])
#HORA, MINUTOS E SEGUNDOS DO DIA FINAL
hh_f,mm_f,ss_f = input().split(':')
hh_f = int(hh_f)
mm_f = int(mm_f)
ss_f = int(ss_f)

W = n_dias_f - n_dias_i
X= hh_f - hh_i
if (X < 0):
    X += 24
    W -= 1
Y = mm_f - mm_i
if (Y < 0):
    Y += 60
    X -= 1
Z = ss_f - ss_i
if(Z < 0):
    Z += 60
    Y -= 1
if (W <= 0):
    W = 0
print('{} dia(s)'.format(W))
print('{} hora(s)'.format(X))
print('{} minuto(s)'.format(Y))
print('{} segundo(s)'.format(Z))