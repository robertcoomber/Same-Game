# This module will intake commands and call the appropriate functions
# Utilizes the game_state object and agent object

from same_game import agent, game_state, searches, metrics
from copy import deepcopy

def agentVSPlayer():
    while True:
        print("Welcome to the Same Game!")
        print("The goal of this game is to remove as many color groupings of 2 or more tiles as possible.")
        print("The bigger the group you remove, the more points you score! Try to score as high as you can.")
        print("")
        name = input("What is your name? ")
        size = int(input("What size board would you like to play on? (enter a single number. i.e. 5 = a 5x5 board) "))
        colors = int(input("How many different colors would you like? (Recommended 3 or more) "))
        board = game_state.State(name, size, colors)
        board2 = deepcopy(board)
        while board.movesLeft():
            metrics.playerMoves += 1
            print("Move", metrics.playerMoves)
            print(board.data, '\n')
            print('Current Score:', board.score, '\n')
            print("Moves:")
            for i in range(len(board.moves())):
                print(i, ")", board.moves()[i])
            x = int(input("\nYour move: "))
            board.remove(board.moves()[x])
        print("Final Board:")
        print(board.data)
        print()
        print("Now lets see how the agent did...")
        ag = agent.Agent(board2)
        searches.breadth_first_tree_search(ag)
        print('Final board:\n', board2.data, '\n')
        print('Agent Scored:', board2.score, '\n')
        if(input("Play again? (y/n) ") == 'n'):
            break





# runs search algorithms on a list of boards, reporting the metrics for each
def agentOnlyMetrics(boards):
    print('Agent metrics on set of input same-game boards:')
    print('-----------------------------------------------')
    for board in boards:
        boardCopy = deepcopy(board)
        ag = agent.Agent(board)
        ag2 = agent.Agent(boardCopy)
        print('Starting board:\n', board.data, '\n')
        searches.breadth_first_tree_search(ag)
        print('Final board (breadth first):\n', board.data, '\n')
        print('Moves:')
        count = 1
        for move in ag.movesList:
            print(count, ': ', move)
            count += 1
        print('Total score:', board.score, '\n')
        searches.depth_first_tree_search(ag2)
        print('Final board (depth first):\n', boardCopy.data, '\n')
        print('Moves:')
        count = 1
        for move in ag2.movesList:
            print(count, ': ', move)
            count += 1
        print('Total score:', boardCopy.score, '\n')


if __name__ == '__main__':
    agentVSPlayer()








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
