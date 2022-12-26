import os
import csv
import random
import shutil
from ga import *

#table[x][y] -> time for machine x doing jobs y
# table = [[1, 2], 
#         [4, 8]]

#jobs[x] -> machine x do jobs[x]

def run_ga(solution: genetic_algorithm):
    for _ in range(gaParameter['liveLoops']):
        solution.crossover()
        solution.mutation()
        solution.selection()
        solution.update_best()
        solution.plt.append('best', solution.bestSolTimes)
        # print(solution.bestSolTimes)
    # 跑多次 找 平均 標準差 收斂

def rm(path: str):
    shutil.rmtree(f'figure/{path}')
    os.mkdir(f'figure/{path}')

def remove_exist_file():
    rm('best')
    rm('minmax')

def draw_plt(bestSolTime: list):
    plt.plot(bestSolTime)
    plt.title('every loops best value')
    plt.xlabel('loop i')
    plt.ylabel('best value')  
    plt.savefig(f'figure/every-loop-best.png')
    print(f'avrage: {np.average(bestSolTime)} std: {np.std(bestSolTime)}')

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
        'liveLoops' : 50,
        'jap' : japProblem,
        'popSize' : 5,
        'geneSize' : len(table),
        'mutationRate' : 0.1,
        'selectionRate' : 0.1,
        'mutationType' : mutation_type.Inversion,
        'selectionType' : selection_type.Deterministic,
        'crossoverType' : crossover_type.PartialCrossover
    }

    loops = 10
    data = []
    bestSolTime = []
    remove_exist_file()
    
    for i in range(loops):
        solution = genetic_algorithm(gaParameter)
        solution.initialize()
        run_ga(solution)
        data.append(solution.plt)
        data[i].show(show_type.Best, i)
        data[i].show(show_type.MinMax, i)
        print(f'loop {i} best Solution: {solution.bestSol}, time: {solution.bestSolTimes}')
        bestSolTime.append(solution.bestSolTimes)

    draw_plt(bestSolTime)
