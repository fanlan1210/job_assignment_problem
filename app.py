import random
import matplotlib.pyplot as plt
from ga import *

n, popSize = 2, 10
table = [[random.randint(1, 100) for i in range(n)] for j in range(n)]
#table[x][y] -> time for machine x doing jobs y
table = [[1, 2], 
        [4, 8]]
# ga_sol(table, n, m)

dd = jap(table)
jobs = [ x for x in range(n)]
#jobs[x] -> machine x do jobs[x]
print(dd.compute_times(jobs[::-1]))

# plt.plot(test)
# plt.show()