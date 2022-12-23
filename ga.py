from enum import Enum
import random
import numpy as np

class jap():
    def __init__(self, timeTable):
        self.timeTable = timeTable
    def compute_times(self, jobs):
        val = 0
        for i, v in enumerate(jobs):
            val += self.timeTable[i][v]
        return val

class crossover_type(Enum) :
    PartialCrossover = 1
    OrderCrossover = 2
    PositionBasedCrossover = 3

class mutation_type(Enum):
    Inversion = 1
    Insertion = 2
    Displacement = 3
    ReciprocalExchange = 4
    
class selection_type(Enum):
    Deterministic = 1
    Stochastic= 2

class genetic_algorithm():
    def __init__(self, parameter):
        self.jap = parameter['jap']
        self.popSize = parameter['popSize']
        self.geneSize = parameter['geneSize']
        self.mutationRate = parameter['mutationRate']
        self.selectionRate = parameter['selectionRate']
        self.mutationType = mutation_type['Insertion']
        self.selectionType = selection_type['Deterministic']
        self.crossoverType = crossover_type['OrderCrossover']
    
    def initialize(self):
        self.chromosome = np.zeros((self.popSize, self.geneSize), dtype=int)
        for i in range(self.popSize):
            self.chromosome[i] = np.random.permutation(self.geneSize)
            # print(self.chromosome[i])
        self.fitness = np.zeros(self.popSize, dtype=int)
        self.compute_fitness()
        # print(self.fitness)
    
    def compute_fitness(self):
        for i in range(self.popSize):
            self.fitness[i] = self.jap.compute_times(self.chromosome[i])
        maxinum = np.max(self.fitness)
        # print(maxinum)
        # print(self.fitness)
        # print("fitness")
        for i in range(self.popSize):
            self.fitness[i] = maxinum - self.fitness[i]
        # print(self.fitness)