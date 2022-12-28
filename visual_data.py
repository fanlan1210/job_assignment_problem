import numpy as np
from enum import Enum
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


class show_type(Enum):
    Best = 1
    MinMax = 2

class visual_data():
    def __init__(self):
        self.data = {}
    def append(self, arg:str, nums:int):
        if arg not in self.data:
            self.data[arg] = []
        self.data[arg].append(nums)

    def show_best(self, i: int):
        plt.plot(self.data['best'], label='best', marker='o')
        plt.title('best value')
        plt.xlabel('iteration')
        plt.ylabel('cost')                                
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        minIdx = np.argmin(self.data['best'])
        plt.annotate('{}'.format(self.data['best'][minIdx]), xy=(minIdx, self.data['best'][minIdx]), xytext=(minIdx, self.data['best'][minIdx] + 2))
        plt.savefig('figure/best/loop%.2d.png' % (i))
        # plt.show()
        plt.close()

    def show_min_max(self, i: int):
        plt.plot(self.data['max'], label='max', marker='o')
        plt.plot(self.data['min'], label='min', marker='o')
        plt.plot(self.data['dif'], label='diff', marker='o')
        plt.title('min and max time')
        plt.xlabel('iteration')
        plt.ylabel('cost')                                
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.legend()
        minIdx = np.argmin(self.data['min'])
        plt.annotate('{}'.format(self.data['min'][minIdx]), xy=(minIdx, self.data['min'][minIdx]), xytext=(minIdx, self.data['min'][minIdx] + 2))
        plt.savefig('figure/minmax/loop%.2d.png' % (i))
        # plt.show()
        plt.close()

    def show(self, type: show_type, i: int):
        if type == show_type.Best:
            self.show_best(i)
        
        if type == show_type.MinMax:
            self.show_min_max(i)