# This module contains the agent class that will perform actions on the game state

import same_game.searches as searches
import same_game.game_state as game_state

class Agent(searches.Problem):

    # Initialize the agent, passing in an initial game state object and goal state
    def init(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    # returns a list of actions on the state
    # state --> a game_state object
    def actions(self, state):
        moves = state.moves()
        return moves

    # performs the remove() function on the state, given the action selected from the returned array of moves
    def result(self, state, action):
        state.remove(action)
        return state

    # calls the isEmpty() method on the state to determine if all squares have been removed from the board
    def goal_test(self, state):
        movesLeft = state.movesLeft()
        movesLeft = not movesLeft
        return movesLeft
