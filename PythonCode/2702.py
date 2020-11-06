frango_disp, bife_disp, massa_disp = map(int, input().split())
frango_pedi, bife_pedi, massa_pedi = map(int, input().split())
n_receberam = 0
if frango_pedi > frango_disp:
    n_receberam += frango_pedi - frango_disp
if bife_pedi > bife_disp:
    n_receberam += bife_pedi - bife_disp
if massa_pedi > massa_disp:
    n_receberam += massa_pedi - massa_disp
print(n_receberam)