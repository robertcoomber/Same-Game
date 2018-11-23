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
        board.moves()
        print('Final board:\n', board.data, '\n')


# runs search algorithms on a list of boards, reporting the metrics for each
# def agentOnlyMetrics(boards):
#     print('Agent metrics on set of input same-game boards:')
#     print('-----------------------------------------------')
#     for board in boards:
#         board2 = deepcopy(board) #makes a placeholder for when it is only adding values within, where it needs to restart from where it left off instead of letting the agent change the board
#         go = True
#         add = True #wether it knows to continue with the adding
#         addLimit = board.size #how many times it will change tiles before generating an entirely new board
#         aL = deepcopy(addLimit) #a placeholder to keep track of how many times it has added
#         boardCount = 0
#         while go:
#             if not add: #this is to generate new random board every "addLimit" times
#                 board.data = board.setup()
#                 #print(board.data)
#                 add = True
#             else:
#                 board.data = deepcopy(board2.data) #these next three lines are when it is fixing the placeholder so the agent doesnt modify what is being passed in
#                 board.changeATile(1)
#                 board2.data = deepcopy(board.data)
#                 #print(board.data)
#                 aL = aL-1
#                 if aL == 0: #if the add counter hits 0, just restart and tell it to regenerate the board
#                     add = False
#                     aL = deepcopy(addLimit)
#             pre = deepcopy(board.data)
#             ag = agent.Agent(board)
#             searches.depth_first_tree_search(ag)
#             post = deepcopy(board.data)
#             if board.isEmpty() == True:
#                 go = False
#                 print('Starting board:\n', pre, '\n')
#                 print('Final board:\n', post, '\n')
#             boardCount = boardCount + 1
#
#         print("Boards generated before correct: ", boardCount, '\n')
#
#
