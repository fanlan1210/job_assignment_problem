import pytest
from app import *

def test_is_child_element_repeat():
    table = None
    japProblem = jap(table, N= 100, MAX_VAL= 10000)

    gaParameter = {
        'jap' : japProblem,
        'popSize' : 5,
        'geneSize' : 1000,
        'mutationRate' : 1,
        'selectionRate' : 0.1,
        'mutationType' : mutation_type.Inversion,
        'selectionType' : selection_type.Deterministic,
        'crossoverType' : crossover_type.OrderCrossover
    }
    
    # with open('data.csv', 'w', newline='') as f:
    #     sap = jap(None, 8, 100)
    #     csvwriter = csv.writer(f)
    #     for i in sap.timeTable:
    #         csvwriter.writerow(i)

    solution = genetic_algorithm(gaParameter)
    solution.initialize()
    solution.crossover()
    solution.mutation()

    n = len(solution.childList)
    chk = [{} for _ in range(n)]
    for i in range(n):
        chk = set()
        for j in range(solution.geneSize):
            if solution.childList[i][j] not in chk:
                chk.add(solution.childList[i][j])
            else:
                print(solution.childList[i])
                raise 'cc'