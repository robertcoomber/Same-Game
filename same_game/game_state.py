import utils
import random
import numpy as np
from same_game import searches

# This module will store information on each iteration of the game,
# and be able to return modifications of the state

# Max 15x15 for the size
# Max 5 colors: Red Orange Yellow Green Blue

class State()

    def __init__(self, name, size, colors):
        self.name = name #String to represent state
        self.size = size #Int between 1-15 for the length and width
        self.colors = colors #Int between 1-5 picking the number of colors
        self.data = self.setup()

    def __init__(self, name, size, colors, data):
        self.name = name  # String to represent state
        self.size = size  # Int between 1-15 for the length and width
        self.colors = colors  # Int between 0-4 picking the number of colors
        self.data = data

    def setup(self):
        ran = random.seed(a=None)
        ran.randint(0, self.colors)
        matrix = np.empty([self.size,self.size])
        for i in range(self.size):
            for ii in range(self.size):
                matrix[i][ii] = ran.randint(1,self.colors+1)
        return matrix

    def getColor(self, x, y):
        if (x < 15):
            if (y < 15):
                return self.data[x][y]

    def sections(self):
        

    def remove(self):




class Square()

    def __init__(self, ):