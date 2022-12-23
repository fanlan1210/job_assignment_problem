import random
import matplotlib.pyplot as plt
from ga import *

n = 5
table = [[random.randint(1, 100) for i in range(n)] for j in range(n)]

#table[x][y] -> time for machine x doing jobs y
# table = [[1, 2], 
#         [4, 8]]

#jobs[x] -> machine x do jobs[x]

gaParameter = {
    'popSize' : 10,
    'geneSize' : n,
    'mutationRate' : 0.1,
    'selectionRate' : 0.1,
    'mutationType' : mutation_type.Insertion,
    'selectionType' : selection_type.Deterministic,
    'crossoverType' : crossover_type.OrderCrossover
}

solution = genetic_algorithm(gaParameter)
solution.initialize()
# print(gaPara)
# 跑多次 找 平均 標準差 收斂