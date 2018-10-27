import utils
import random
import numpy as np
from same_game import searches

# This module will store information on each iteration of the game,
# and be able to return modifications of the state

# Max 15x15 for the size
# Max 5 colors: Red Orange Yellow Green Blue

class State:

    def __init__(self, name, size, colors, data=np.zeros([1,1])):
        self.name = name  # String to represent state
        self.size = size  # Int between 1-15 for the length and width
        self.colors = colors  # Int between 1-5 picking the number of colors
        if np.array_equal(data, np.zeros([1,1])):
            data = self.setup()
        self.data = data
        self.memory = []

    # def __init__(self, name, size, colors, data):
    #     self.name = name  # String to represent state
    #     self.size = size  # Int between 1-15 for the length and width
    #     self.colors = colors  # Int between 0-4 picking the number of colors
    #     self.data = data

    def setup(self):
        matrix = np.empty([self.size,self.size])
        for row in range(self.size):
            for col in range(self.size):
                matrix[row][col] = random.randint(1,self.colors)
        return matrix

    def getColor(self, x, y):
        if x < 15:
            if y < 15:
                return self.data[x][y]

    def sections(self):
        self.memory = []
        moves = []
        for row in range(self.size):
            for col in range(self.size):
                if self.data[row, col] != 0:
                    if [row, col] not in self.memory:
                        self.memory.append([row,col])
                        move = self.recSections([row,col], self.memory, [])
                        moves.append([[row,col], move])
        return moves

    def recSections(self, current, memory, move):
        move1, move2, move3, move4 = [], [], [], []
        if current[0]-1 >= 0:
            if self.data[current[0]][current[1]] == self.data[current[0]-1][current[1]] and [current[0]-1,current[1]] not in self.memory:
                self.memory.append([current[0]-1, current[1]])
                move1 = self.recSections([current[0] - 1, current[1]], self.memory, move1)
                move1.append([current[0]-1, current[1]])
        if current[0]+1 < self.size:
            if self.data[current[0]][current[1]] == self.data[current[0]+1][current[1]] and [current[0]+1,current[1]] not in self.memory:
                self.memory.append([current[0]+1, current[1]])
                move2 = self.recSections([current[0]+1, current[1]], self.memory, move2)
                move2.append([current[0]+1, current[1]])
        if current[1]-1 >= 0:
            if self.data[current[0]][current[1]] == self.data[current[0]][current[1]-1] and [current[0], current[1]-1] not in self.memory:
                self.memory.append([current[0], current[1]-1])
                move3 = self.recSections([current[0], current[1]-1], self.memory, move3)
                move3.append([current[0], current[1]-1])
        if current[1]+1 < self.size:
            if self.data[current[0]][current[1]] == self.data[current[0]][current[1]+1] and [current[0], current[1]+1] not in self.memory:
                self.memory.append([current[0], current[1]+1])
                move4 = self.recSections([current[0], current[1]+1], self.memory, move4)
                move4.append([current[0], current[1]+1])
        return move1 + move2 + move3 + move4


#     def remove(self):
#
#
#
#
# class Square()
#
#     def __init__(self, ):