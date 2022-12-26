import random
import csv
import matplotlib.pyplot as plt
from ga import *

#table[x][y] -> time for machine x doing jobs y
# table = [[1, 2], 
#         [4, 8]]

#jobs[x] -> machine x do jobs[x]


if __name__ == '__main__':
    table = None
    try:
        with open('data.csv', 'r') as f:
            csvReader = csv.reader(f)
            table = list(csvReader)
    except:
        pass

    japProblem = jap(table)

    gaParameter = {
        'loops' : 20,
        'jap' : japProblem,
        'popSize' : 5,
        'geneSize' : len(table),
        'mutationRate' : 1,
        'selectionRate' : 0.1,
        'mutationType' : mutation_type.Inversion,
        'selectionType' : selection_type.RouletteWheel,
        'crossoverType' : crossover_type.PartialCrossover
    }
    # for _ in range(parameter['loops']):
    solution = genetic_algorithm(gaParameter)
    solution.initialize()
    solution.crossover()
    solution.mutation()
    solution.compute_fitness()
    solution.selection()
    # 跑多次 找 平均 標準差 收斂