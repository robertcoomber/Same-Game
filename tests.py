from same_game import game_state as state

testArray = state.State("testArray", 2, 2)
print("The generated board:")
print(testArray.data)
print("Possible moves:")
print(testArray.sections())
