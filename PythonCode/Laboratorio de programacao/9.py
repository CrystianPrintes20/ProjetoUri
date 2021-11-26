from statistics import pstdev, mean
vetor = [2,3,6,21,23,4,5,7,8,10]
media = mean(vetor)
valor = pstdev(vetor, media)
print('O desvio de padrão é:',valor)

'''import math, statistics
# We relay on our previous implementation for the variance
def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)
...

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    print(std_dev)

stdev([2,3,6,21,23,4,5,7,8,10])

valor = statistics.pstdev([2,3,6,21,23,4,5,7,8,10])
print(valor)'''