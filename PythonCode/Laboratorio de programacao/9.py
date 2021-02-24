'''
from statistics import pstdev, mean, stdev

vetor = [0,1,2,3,4,5,6,7,8,9]

media = mean(vetor)
print(media)
valor = pstdev(vetor, media)
valor1 = stdev(vetor, media)
print(valor)
print(valor1)'''

import math, statistics
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

stdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])

valor = statistics.pstdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])
print(valor)