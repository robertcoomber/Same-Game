import time

playerScore = 0
playerMoves = 0
agentScore = 0
agentMoves = 0

# dictionary of clocks
references = {}

#pass in a reference so that it can save the specific time to a dicitonary, and then compare it to the end time once the reference is passed in again
def startTime(reference):
    references[str(reference)] = time.time()

# will return a float of the time passed
def getTime(reference):
    elapsed = 0
    if str(reference) in references:
        elapsed = time.time() - references[str(reference)]
    print("Seconds elapsed:", elapsed)
    return elapsed

if __name__ == '__main__':
    startTime("key")
    time.sleep(1.3445)
    getTime("key")