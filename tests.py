from same_game import game_state as state

testArray = state.State("testArray", 10, 2)
print("The generated board:")
print(testArray.data)
print("Possible moves:")
print(testArray.sections())
print("The amount of blocks removed for every action:")
for i in range(10): # THIS WILL RESULT IN ERROR IF THE NUMBER IS TOO HIGH, BECAUSE IT DOESNT CHECK TO SEE IF THERE ARE NO MOVES LEFT
    print(testArray.count(testArray.sections()[0]))
    testArray.remove(testArray.sections()[0])
print("Final:")
print(testArray.data)