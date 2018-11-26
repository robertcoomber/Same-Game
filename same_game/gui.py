from graphics import *
from same_game import metrics

win = GraphWin("Same Game", 500, 500)
name = ''

def waitTillClick(p1, p2):
    click = Point(501,501)
    while (click.getX() < p1.getX() or click.getX() > p2.getX()) and (click.getY() < p1.getY() or click.getY() > p2.getY()):
        click = win.getMouse()

def waitTillClickSections(boxes):
    click = win.getMouse()
    out = False
    while True:
        index = 0
        for b in boxes:
            if click.getX() >= b.getP1().getX() and click.getX() <= b.getP2().getX() and click.getY() >= b.getP1().getY() and click.getY() <= b.getP2().getY():
                return index
            index += 1
        click = win.getMouse()

def waitTillAnyClick():
    win.getMouse()
    return

def getName():
    prompt = Text(Point(250, 230),
                "Please enter your name:")
    inputBox = Entry(Point(250, 250), 50)
    inputBox.draw(win)
    prompt.draw(win)
    go1 = Point(230, 270)
    go2 = Point(270, 290)
    go = Rectangle(go1, go2)
    goTxt = Text(Point(250, 280),
                  "Enter")
    go.draw(win)
    goTxt.draw(win)
    waitTillClick(go1, go2)
    name = inputBox.getText()
    go.undraw()
    goTxt.undraw()
    inputBox.undraw()
    prompt.undraw()
    return name

def getSize():
    prompt = Text(Point(250, 230),
                "What size board would you like to play on?")
    prompt.draw(win)
    go0 = Rectangle(Point(240,250), Point(260,270))
    go0Txt = Text(Point(250, 260),"3")
    go0.draw(win)
    go0Txt.draw(win)
    go1 = Rectangle(Point(240, 275), Point(260, 295))
    go1Txt = Text(Point(250, 285), "4")
    go1.draw(win)
    go1Txt.draw(win)
    go2 = Rectangle(Point(240, 300), Point(260, 320))
    go2Txt = Text(Point(250, 310), "5")
    go2.draw(win)
    go2Txt.draw(win)
    go3 = Rectangle(Point(240, 325), Point(260, 345))
    go3Txt = Text(Point(250, 335), "6")
    go3.draw(win)
    go3Txt.draw(win)
    index = waitTillClickSections([go0, go1, go2, go3])
    go0.undraw()
    go0Txt.undraw()
    go1.undraw()
    go1Txt.undraw()
    go2.undraw()
    go2Txt.undraw()
    go3.undraw()
    go3Txt.undraw()
    prompt.undraw()
    if index == 0:
        return 3
    elif index == 1:
        return 4
    elif index == 2:
        return 5
    elif indexx == 3:
        return 6

def updateBoard(board):
    return 0

def updateAgentBoard(board):
    return 0

def finalBoard(board):
    return 0

def finalAgentBoard(board):
    return 0

def results():
    return 0

def intro():
    hello = Text(Point(250,200), "Welcome to the Same Game!")
    goal = Text(Point(250, 230), "The goal of this game is to remove as many color groupings of 2 or more tiles as possible.")
    points = Text(Point(250, 260), "The bigger the group you remove, the more points you score! Try to score as high as you can.")
    n = Text(Point(250, 290),
                  "Click anywhere to continue...")
    hello.draw(win)
    goal.draw(win)
    points.draw(win)
    n.draw(win)

    win.getMouse()
    hello.undraw()
    goal.undraw()
    points.undraw()
    n.undraw()
    return

if __name__ == '__main__':
    intro()
    getName()
    print(getSize())
    waitTillAnyClick()

