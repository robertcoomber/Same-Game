from same_game import game_state as state
from same_game import controller

def test_game_state():
    testArray = state.State("testArray", 10, 4)
    print("The generated board:")
    print(testArray.data)
    print("All Sections:")
    print(testArray.sections())
    print("Valid Moves:")
    print(testArray.moves())
    print("The moves left and amount of blocks removed for every action:")
    for i in range(20):
        if testArray.isEmpty() == False and testArray.movesLeft():
            print(testArray.moves())
            print(testArray.count(testArray.moves()[0]))
            testArray.remove(testArray.moves()[0])
    print("Final:")
    print(testArray.data)
    print('Is the board empty?')
    print(testArray.isEmpty(),'\n')

def test_controller():
    testBoards = [
        state.State("Test1", 4, 2),
        # state.State("Test2", 7, 3),
    ]

    controller.agentOnlyMetrics(testBoards)


# Call functions here to run specific tests
test_game_state()
test_controller()
