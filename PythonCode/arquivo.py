"""r -> usado somente para ler algo
   w -> usado para escrever algo
   r+ -> usado para ler e escrever algo
   a -> usado para acrescentar algo"""
for i in range(1008,2000):
    arquivo = open(str(i)+'.py', 'w')
    arquivo.close()