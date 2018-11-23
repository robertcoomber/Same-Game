# This module will intake commands and call the appropriate functions
# Utilizes the game_state object and agent object

from same_game import agent, game_state, searches
from copy import deepcopy

# runs search algorithms on a list of boards, reporting the metrics for each
def agentOnlyMetrics(boards):
    print('Agent metrics on set of input same-game boards:')
    print('-----------------------------------------------')
    for board in boards:
        ag = agent.Agent(board)
        print('Starting board:\n', board.data, '\n')
        searches.breadth_first_tree_search(ag)
        print('Final board:\n', board.data, '\n')

