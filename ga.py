from enum import Enum

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

# class genetic_algorithm():
    # def __init__(self, ):