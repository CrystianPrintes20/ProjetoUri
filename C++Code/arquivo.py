"""r -> usado somente para ler algo
   w -> usado para escrever algo
   r+ -> usado para ler e escrever algo
   a -> usado para acrescentar algo"""
for i in range(1000,1010):
    arquivo = open(str(i)+'.cpp', 'w')
    arquivo.close()