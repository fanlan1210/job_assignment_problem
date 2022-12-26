import copy
import random
import numpy as np
from enum import Enum
from visual_data import *

class jap():
    def __init__(self, timeTable: list = None, N: int = 10, MAX_VAL: int = 10):
        if timeTable == None:
            timeTable = [[random.randint(1, MAX_VAL) for i in range(N)] for j in range(N)]
        else:
            timeTable = [[int(x) for x in i] for i in timeTable]
        self.timeTable = timeTable
        random.seed()

    def compute_times(self, jobs):
        val = 0
        for i, v in enumerate(jobs):
            val += self.timeTable[i][v]
        return val

class crossover_type(Enum) :
    PartialCrossover = 1

class mutation_type(Enum):
    Inversion = 1
    Swap = 2
    
class selection_type(Enum):
    Deterministic = 1
    RouletteWheel = 2

class genetic_algorithm():
    def __init__(self, parameter):
        self.jap = parameter['jap']
        self.popSize = parameter['popSize']
        self.geneSize = parameter['geneSize']
        self.mutationRate = parameter['mutationRate']
        self.selectionRate = parameter['selectionRate']
        self.mutationType = parameter['mutationType']
        self.selectionType = parameter['selectionType']
        self.crossoverType = parameter['crossoverType']
    
    def initialize(self):
        self.plt = visual_data()
        self.chromosome = np.zeros((self.popSize, self.geneSize), dtype=int)
        for i in range(self.popSize):
            self.chromosome[i] = np.random.permutation(self.geneSize)
        self.bestSol = self.chromosome[0]
        self.bestSolTimes = self.jap.compute_times(self.bestSol)

    def update_best(self):
        mn = 99999999
        mx = -1
        for i in range(self.popSize):
            curTime = self.jap.compute_times(self.chromosome[i])
            mn = min(mn, curTime)
            mx = max(mx, curTime)
            if curTime < self.bestSolTimes:
                self.bestSolTimes = curTime
                self.bestSol = self.chromosome[i]
        self.plt.append('min', mn)
        self.plt.append('max', mx)

    def compute_fitness(self):
        self.fitness = np.zeros(np.size(self.chromosome, 0), dtype=int)
        for i in range(np.size(self.chromosome, 0)):
            self.fitness[i] = self.jap.compute_times(self.chromosome[i])
        maxinum = np.max(self.fitness)
        for i in range(np.size(self.chromosome, 0)):
            self.fitness[i] = max(1, maxinum - self.fitness[i])

    def getRndRange(self):
        leftBound = random.randint(0, self.geneSize - 2)
        rightBound = random.randint(leftBound + 1, self.geneSize - 1)
        return leftBound, rightBound

    def shuffle(self):
        pass

    def partial_crossover(self, p1: int, p2: int):
        childList = self.childList
        leftBound, rightBound = self.getRndRange()
        c1 = copy.deepcopy(self.chromosome[p1])
        c2 = copy.deepcopy(self.chromosome[p2])

        for i in range(leftBound, rightBound + 1):
            c1[i], c2[i] = c2[i], c1[i]

        cxNumToIdx = [dict() for _ in range(2)]
        cxRepeat = [list() for _ in range(2)]

        for i in range(self.geneSize):
            if c1[i] not in cxNumToIdx[0]:
                cxNumToIdx[0][c1[i]] = i
            elif leftBound <= i <= rightBound:
                cxRepeat[0].append(cxNumToIdx[0][c1[i]])
            else:
                cxRepeat[0].append(i)

            if c2[i] not in cxNumToIdx[1]:
                cxNumToIdx[1][c2[i]] = i
            elif leftBound <= i <= rightBound:
                cxRepeat[1].append(cxNumToIdx[1][c2[i]])
            else:
                cxRepeat[1].append(i)
        
        for i, j in zip(cxRepeat[0], cxRepeat[1]):
            c1[i], c2[j] = c2[j], c1[i]
        
        childList.append(c1)
        childList.append(c2)
        
    def crossover(self):
        self.childList = []
        rng = self.popSize - self.popSize % 2
        self.chromosome = np.random.permutation(self.chromosome)
        for i in range(0, rng, 2):
            if self.crossoverType == crossover_type.PartialCrossover:
                self.partial_crossover(i, i + 1)
        self.chromosome = np.concatenate((self.chromosome, np.array(self.childList)))

    def mutationInverse(self, idx):
        leftBound, rightBound = self.getRndRange()
        self.chromosome[idx][leftBound:rightBound + 1] = self.chromosome[idx][leftBound:rightBound + 1][::-1]

    def mutationSwap(self, idx):
        sa = random.randint(0, self.geneSize - 2)
        sb = random.randint(sa + 1, self.geneSize - 1)
        gene = self.chromosome[idx]
        gene[sa], gene[sb] = gene[sb], gene[sa]

    def mutation(self):
        for i in range(np.size(self.chromosome, 0)):
            if random.randint(0, 100) <= self.mutationRate * 100:
                if self.mutationType == mutation_type.Inversion:
                    self.mutationInverse(i)
                if self.mutationType == mutation_type.Swap:
                    self.mutationSwap(i)
    
    def selectionDeterministic(self):
        lst = sorted(range(len(self.fitness)), key=lambda k: self.fitness[k])
        a = [self.chromosome[i] for i in lst[::-1]]
        self.chromosome = np.array(a[:self.popSize])

    def selectionRouletteWheel(self):
        self.fitness = self.fitness / np.sum(self.fitness)
        self.chromosome = self.chromosome[np.random.choice(np.size(self.chromosome, 0), self.popSize, replace=False, p=self.fitness)]

    def selection(self):
        self.compute_fitness()
        if self.selectionType == selection_type.Deterministic:
            self.selectionDeterministic()

        if self.selectionType == selection_type.RouletteWheel:
            self.selectionRouletteWheel() 