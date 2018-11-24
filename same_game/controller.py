# This module will intake commands and call the appropriate functions
# Utilizes the game_state object and agent object

from same_game import agent, game_state, searches, metrics
from copy import deepcopy

def displayMetrics(reference):
    metric = metrics.getMetrics(reference.__repr__())
    moves = metric[0]
    score = metric[1]
    depth = metric[2]
    nodes = metric[3]
    time = metric[4]
    print('Moves:')
    count = 1
    for move in moves:
        print(count, ': ', move)
        count += 1
    print("-----------------------------------------")
    print('Total score:', score)
    print('Depth of solution:', depth)
    print('Number of nodes explored:', nodes)
    print('Seconds taken:', time)

def runSearch(reference, board):
    ag = agent.Agent(board)
    print('Starting board (', reference, '):\n', board.data)
    metrics.startTime(board.__repr__())
    if reference == "depth":
        result = searches.depth_first_tree_search(ag)
    if reference == "breadth":
        result = searches.breadth_first_tree_search(ag)
    time = metrics.getTime(board.__repr__())
    path = result.path()
    moves = []
    for node in path:
        if node.action:
            moves.append(node.action)
    metrics.setMetrics(board.__repr__(), moves, result.state.score, result.depth, ag.nodesExplored, time)
    metrics.agentScore = result.state.score
    print('Final board (', reference, '):\n', result.state.data)



def agentVSPlayer():
    while True:
        print("Welcome to the Same Game!")
        print("The goal of this game is to remove as many color groupings of 2 or more tiles as possible.")
        print("The bigger the group you remove, the more points you score! Try to score as high as you can.")
        print("")
        name = input("What is your name? ")
        size = int(input("What size board would you like to play on? (enter a single number. i.e. 5 = a 5x5 board) "))
        colors = int(input("How many different colors would you like? (Recommended 2 or more) "))
        search = ""
        while search != "breadth" and search != "depth":
            search = input("What search would you like? (breadth or depth)")
        boardp = game_state.State(name, size, colors)
        boarda = deepcopy(boardp)
        while boardp.movesLeft():
            metrics.playerMoves += 1
            print("Move", metrics.playerMoves)
            print(boardp.data)
            print('Current Score:', boardp.score)
            print("Choose a move #:")
            for i in range(len(boardp.moves())):
                print(i, ")", boardp.moves()[i])
            x = int(input("Your move: "))
            boardp.remove(boardp.moves()[x])
        metrics.playerScore = boardp.score
        print("Final Board:")
        print(boardp.data)
        print()
        print("Now lets see how the agent did...")
        print(search, "===============================")
        runSearch(search, boarda)
        displayMetrics(boarda)
        print
        print("You scored:", metrics.playerScore)
        print("Agent scored:", metrics.agentScore)
        if metrics.playerScore > metrics.agentScore:
            print("You win!")
        elif metrics.playerScore == metrics.agentScore:
            print("You tied!")
        else:
            print("You lost!")

        if(input("Play again? (y/n) ") == 'n'):
            break

# runs search algorithms on a list of boards, reporting the metrics for each
def agentOnlyMetrics(boards):
    print('Agent metrics on set of input same-game boards:')
    print('-----------------------------------------------')
    for board in boards:
        for s in metrics.searches:
            boardCopy = deepcopy(board)
            runSearch(s, boardCopy)
            displayMetrics(boardCopy)

if __name__ == '__main__':
    agentVSPlayer()

# # THIS IS OLD ONE THAT ISNT EFFICIENT
# def agentOnlyMetrics(boards):
#     print('Agent metrics on set of input same-game boards:')
#     print('-----------------------------------------------')
#     for board in boards:
#         boardCopy = deepcopy(board)
#         ag = agent.Agent(board)
#         ag2 = agent.Agent(boardCopy)
#
#         print('Starting board:\n', board.data, '\n')
#         metrics.startTime(board.__repr__())
#         breadth_result = searches.breadth_first_tree_search(ag)
#         metrics.getTime(board.__repr__())
#         print('Final board (breadth first):\n', breadth_result.state.data, '\n')
#         breadth_path = breadth_result.path()
#         breadth_moves = []
#         for node in breadth_path:
#             if node.action:
#                 breadth_moves.append(node.action)
#         print('Moves:')
#         count = 1
#         for move in breadth_moves:
#             print(count, ': ', move)
#             count += 1
#         print('\nTotal score:', breadth_result.state.score, '\n')
#         print('Depth of solution:', breadth_result.depth, '\n')
#         print('Number of nodes explored:', ag.nodesExplored, '\n')
#
#         print('Starting board:\n', boardCopy.data, '\n')
#         metrics.startTime(boardCopy.__repr__())
#         depth_result = searches.depth_first_tree_search(ag2)
#         metrics.getTime(boardCopy.__repr__())
#         print('Final board (depth first):\n', depth_result.state.data, '\n')
#         depth_path = depth_result.path()
#         depth_moves = []
#         for node in depth_path:
#             if node.action:
#                 depth_moves.append(node.action)
#         print('Moves:')
#         count = 1
#         for move in depth_moves:
#             print(count, ': ', move)
#             count += 1
#         print('\nTotal score:', depth_result.state.score, '\n')
#         print('Depth of solution:', depth_result.depth, '\n')
#         print('Number of nodes explored:', ag2.nodesExplored, '\n')

# THIS IS OLD ONE WITH THE WEIRD CHECK FOR COMPLETENESS
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
