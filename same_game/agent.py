# This module contains the agent class that will perform actions on the game state

import same_game.searches as searches
import same_game.game_state as game_state
from copy import deepcopy

class Agent(searches.Problem):

    # Initialize the agent, passing in an initial game state object and goal state
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal
        self.movesList = []

    # returns a list of actions on the state
    # state --> a game_state object
    def actions(self, state):
        moves = state.moves()
        return moves

    # performs the remove() function on the state, given the action selected from the returned array of moves
    def result(self, state, action):
        newState = deepcopy(state)
        newState.remove(action)
        self.movesList.append(action)
        # print('checking moves...\n')
        return newState

    # calls the movesLeft() method on the state to determine if no possible moves are remaining
    def goal_test(self, state):
        movesLeft = state.movesLeft()
        movesLeft = not movesLeft
        return movesLeft
