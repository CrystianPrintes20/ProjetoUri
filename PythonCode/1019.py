N = int(input())
horas = N // 3600
resto_h = N % 3600
minutos = resto_h // 60
resto_m = resto_h % 60
segundos = resto_m
print("{:}:{:}:{:}" .format(horas, minutos, segundos))