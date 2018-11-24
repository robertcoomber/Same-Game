import time

playerScore = 0
playerMoves = 0
playerTime = 0
agentScore = 0
agentMoves = 0

# dictionary of clocks
references = {}
allMetrics = {}
allResults = {}

searches = ['breadth', 'depth', 'flounder', 'greedy']

#pass in a reference so that it can save the specific time to a dicitonary, and then compare it to the end time once the reference is passed in again
def startTime(reference):
    references[str(reference)] = time.time()

# will return a float of the time passed
def getTime(reference):
    elapsed = 0
    if str(reference) in references:
        elapsed = time.time() - references[str(reference)]
    return elapsed

def setMetrics(reference, moves, score, depth, nodes, time):
    allMetrics[str(reference)] = [moves, score, depth, nodes, time]

# stores the metrics within a dictionary of lists with keys of each search that return a list of results
def saveResults(search, reference, moves, score, depth, nodes, time):
    if search in allResults:
        allResults[search] = allResults[search].append([reference, moves, score, depth, nodes, time])
    else:
        allResults[search] = [[reference, moves, score, depth, nodes, time]]

def getResults(search):
    return allResults[search]

def getMetrics(reference):
    return allMetrics[str(reference)]

if __name__ == '__main__':
    startTime("key")
    time.sleep(1.3445)
    getTime("key")