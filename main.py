
# F(n)=G(n)+H(n)

#A* path algorithm
# node is the letter
# edges connect nodes
# a grid 2x2 you can draw it like a graph format which are nodes and the edges connect them
# a weighted edge takes a certain length
# no weighted wedges ... all weight 1
# A* goal is to find the shortest path from A to B in a graph using the edges in that graph
# informed search algorithm with a heuristic function that guides us and figure out the correct path to go down
# we only consider paths that are optimal
# to start we take our START NODE "A" and put it in our open set represented by a Priority Queue
# Open set keeps track of the nodes we want next
# we always start by putting start node in set along with the distance to that node which is our "F score"
# H(n) or "H score" is simply a function that gives us from node "n" to the end node / checking absolute distance (USING MANHATAN DISTANCE)
# G(n) is the current shortest distance from the start node to point C that we currently found
#F(n) = estimate of G(n) + H / trying to give an estimate of taking two blocks to get to this node and from this nodes we think
#   it should take 5 more nodes so a total of 7, should we start looking at this one first or conisder the next node with a
#       lower F Score

# G score is the exact and shortest distance we found currently to get from the start node to whatever node we are talking about
#H score is the heuristic or guess of how far away the node is from the end node

#we assume the next nodes distance is infinity

import pygame
import math
from queue import PriorityQueue
import time
import random
# startTime=time.time()
# lastTime=startTime
# lapnum=1
# value=""


# Setting up the display
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
# pygame.display.set_caption("A* Path Finding Algorithm")
pygame.display.set_caption("MENU -> CHOOSE A LABYRINTH")

fBarriers1AStar = open('A1.txt', 'r+')
fBarriers2AStar = open('A2.txt', 'r+')
fBarriers3AStar = open('A3.txt', 'r+')
fBarriers4AStar = open('A4.txt', 'r+')
fBarriers1Dijkstra = open('dijkstra1.txt', 'r+')
fBarriers2Dijkstra = open('dijkstra2.txt', 'r+')
fBarriers3Dijkstra = open('dijkstra3.txt', 'r+')
fBarriers4Dijkstra = open('dijkstra4.txt', 'r+')
firstLab=open('firstLab.txt','r+')
secondLab=open('secondLab.txt','r+')
thirdLab=open('thirdLab.txt','r+')
fourthLab=open('fourthLab.txt','r+')


#COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

#main visualization grid
class Node:
    #hold where it is, what the width of itself is, and track of all adjacentNodes
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = GREY
        self.adjacentNodes = []
        self.width = width
        self.total_rows = total_rows

    # indexing things using rows and columns
    def returnCurrentPosition(self):
        return self.row, self.col

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.width))

    def barrierIsTrue(self):
        return self.color == BLACK

    def generateBarrierColor(self):
        self.color = BLACK

    def rootNodeColor(self):
        self.color = ORANGE
        # self.color=ORANGE

    def goalNodeColor(self):
        self.color = GREEN
        #self.color=TURQUOISE

    def bestPathColor(self):
        self.color = GREEN
        # self.color = PURPLE

    def checkedNodesColor(self):
        self.color = BLUE

    def nodesInProximityColor(self):
        self.color = TURQUOISE
        # self.color = GREEN

    def updateAdjacentNodes(self, grid): #inside of spot that will add into the neighbors list all of the valid squares that can be neighbors
        #check up down left right and see if those are barriers, and if not add them
        self.adjacentNodes=[]
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].barrierIsTrue():  # DOWN
            self.adjacentNodes.append(grid[self.row + 1][self.col]) #add 1 to the row to go down a row to check if you can move there
                                                                #if you can, append the next row down
        if self.row > 0 and not grid[self.row - 1][self.col].barrierIsTrue():  # UP
            self.adjacentNodes.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].barrierIsTrue():  # RIGHT
            self.adjacentNodes.append(grid[self.row][self.col + 1]) #moving to the right checking the next square and append it to neighbors

        if self.col > 0 and not grid[self.row][self.col - 1].barrierIsTrue():  # LEFT
            self.adjacentNodes.append(grid[self.row][self.col - 1])

        def __lt__(self, other):
            return False


    # LESS THAN, how we handle what happens if we compare 2 spots together.
    def __lt__(self, other):
        return False

def DijstrasAlg(draw, grid, rootNode, goalNode):
    index = 0
    # initialize open list that uses priorityQueue API
    openList = PriorityQueue()
    openList.put((0, index, rootNode))
    closedList = {}
    gScore = {spot: float("inf") for row in grid for spot in row}
    gScore[rootNode] = 0
    fScore = {spot: float("inf") for row in grid for spot in row}
    x1, y1 = rootNode.returnCurrentPosition()
    x2, y2 = goalNode.returnCurrentPosition()
    # Manhattan distance is "abs(x1 - x2) + abs(y1 - y2)"
    fScore[rootNode] = abs(x1 - x2) + abs(y1 - y2)

    hash = {rootNode}
    while not openList.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = openList.get()[2]
        hash.remove(current)
        if current == goalNode:
            drawOptimalPath(closedList, goalNode, draw)
            goalNode.goalNodeColor()
            return True
        for adjacent in current.adjacentNodes:
            tempGScore = gScore[current] + 1
            if tempGScore < gScore[adjacent]:
                closedList[adjacent] = current
                gScore[adjacent] = tempGScore
                x1A, y1A = adjacent.returnCurrentPosition()
                x2, y2 = goalNode.returnCurrentPosition()
                # FScore=GScore is the difference for Dijkstra's which is only the Gscore and uses no heuristic
                fScore[adjacent] = tempGScore

                if adjacent not in hash:
                    index += 1
                    openList.put((fScore[adjacent], index,adjacent))
                    hash.add(adjacent)
                    adjacent.nodesInProximityColor()
        draw()
        if current != rootNode:
            current.checkedNodesColor()

    return False

def drawOptimalPath(closedList, currentNode, draw):
	while currentNode in closedList: # the current node starts at the end node, traverse from end node back to the start node
		currentNode = closedList[currentNode] # current will be equal to whatever we came from
		currentNode.bestPathColor() #make that node part of the path
		draw() # once we get to the node that came from the start node and hit the start node, it will stop reconstructing path

def AStarAlg(draw, grid, rootNode, goalNode):
    index=0
    #initialize open list that uses priorityQueue API
    openList=PriorityQueue()
    openList.put((0, index, rootNode)) #api for priority queue instead of push / add start node with its F-score "0" and
                        # count as 0 to keep track when the items are inserted
                        # put() and get() are nice applications from priorityQueue
    #initialize closedList
    closedList={}#track of where it came from or "path"
    # F(n)=G(n)+H(n)
    # G(n) is the current shortest distance from the start node to point C that we currently found
    gScore = {spot: float("inf") for row in grid for spot in row}
    gScore[rootNode]=0
    fScore = {spot: float("inf") for row in grid for spot in row}
    #get node positions so that we can use that to find manhattan distance
    x1, y1 = rootNode.returnCurrentPosition()
    x2, y2 = goalNode.returnCurrentPosition()
    #Manhattan distance is "abs(x1 - x2) + abs(y1 - y2)"
    fScore[rootNode]= abs(x1 - x2) + abs(y1 - y2)#  heuristic becuase we just want to estimate how far the nodes are
                # Heuristic will just be the approximation

    hash={rootNode} # making a set of rootNode because because priorityQueue() has nothing to tell us if there is a node is in the queue or not and need to check if there is a value there or not
#                         #this will keep track of all items in priority queue and items that aren't
#                         # i can remove an item from the priority queue but I can't check if something is in
#                         # the priority queue
#                         #Here i can check because it will only be a hash that stores everything from the priority queue
#                         #this hash stores everything that the Priority Queue does, but it doesn't have the same dataset implementation giving us the smallest value

    while not openList.empty(): #the alg runs until the open set is empty or not, if it empty all possible nodes have been considered and if
        for event in pygame.event.get(): #path hasnt been found then there is no solution
            if event.type == pygame.QUIT:
                pygame.quit()
        current = openList.get()[2] #indexing at 2 because the open stores the F-score, count, and the node and I just want the node
                                 # pop the priorityQueue value since it will give me the smallest fScore value from openList
        hash.remove(current) # #remove it from hash so we make sure there are no dulicates
        if current == goalNode: #if the node taken from the priority queue is the goal node
            drawOptimalPath(closedList, goalNode, draw) #draw optimal path on purple
            goalNode.goalNodeColor()# recolor the goalnode Turquoise so its visible
            return True
        for adjacent in current.adjacentNodes: # if ajdacent node is in our adjacentNodes list
            tempGScore = gScore[current] + 1 #we can assume all edges are 1, if we want to figure out the tempGScore is we take the distances from the current node and the currently known distance
                                                # and add 1 to it because we are going one node over which is the neighbor of this node
            if tempGScore < gScore[adjacent]: # if we found a better way to reach this neighbor to what we found before, update this path store and keep track of that
                closedList[adjacent]=current #update that adjacent node to the current better node
                gScore[adjacent] = tempGScore #update the score of the adjacent new node
                x1A, y1A = adjacent.returnCurrentPosition() #finding coordinates to use for heuristc below
                x2, y2 = goalNode.returnCurrentPosition()
                # FScore=GScore +Heuristic
                fScore[adjacent] = tempGScore + (abs(x1A - x2) + abs(y1A - y2))
                                                # get pos is the method that gives us the row and column because we need to pass that in
                                                # because the method that passes that in expects 2 positions and not 2 spot objects
                if adjacent not in hash: #to check if the adjacent node is in the oen set or not
                    index+=1 # if it is not in we add it into the set
                    openList.put((fScore[adjacent],index,adjacent)) # put in this new adjacent node because it has a better path
                    hash.add(adjacent) #store the node in there
                    adjacent.nodesInProximityColor() #open because we just put this into the priority queue openLIst
        draw()# you can call draw like this becasue of lambda like "draw = Lambda: print("hello")
        if current != rootNode: # if the node we are traversing through is the starting node
            current.checkedNodesColor() # id the node we just considered is not the start node, we make it red and close it off because we already
                                    #considered and will not be opened back up
    return False

def make_grid(rows,width):
    grid=[]
    gap = width // rows #give us what the gap should be between this rows or what the width of these cubes should be
    for i in range(rows):
        grid.append([]) # 2D list that will have spot objects in them
        for j in range(rows):
            node = Node(i,j, gap, rows) #using new class called Node(), we need to pass its row, column, width, and total amount of rows in the grid and
                            #figure out where it should be sitting
            grid[i].append(node) # in grid row [i], all store nodes
    return grid

def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win,BLACK, (j * gap, 0), (j * gap, width))#flipping the coordinates so we are always top and bottom

def draw(win, grid, rows, width):
	win.fill(GREY)

	for row in grid:
		for node in row:
			node.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()

# -------------------- MENU --------------------------
import sys

def menu():
    pygame.init()

    # Set window size
    size = width, height = 800, 900
    screen = pygame.display.set_mode(size)

    # Clock
    clock = pygame.time.Clock()

    # Load image
    image1 = pygame.image.load('firstLab.png')
    image2 = pygame.image.load('secondLab.png')
    image3 = pygame.image.load('thirdLab.png')
    image4 = pygame.image.load('fourthLab.png')
    titlePNG=pygame.image.load('title.png')

    # Set the size for the image
    DEFAULT_IMAGE_SIZE = (width/2, width/2)

    # Scale the image to your needed size
    titlePNG=pygame.transform.scale(titlePNG,(800,150))
    image1 = pygame.transform.scale(image1, DEFAULT_IMAGE_SIZE)
    image2 = pygame.transform.scale(image2, DEFAULT_IMAGE_SIZE)
    image3 = pygame.transform.scale(image3, DEFAULT_IMAGE_SIZE)
    image4 = pygame.transform.scale(image4, DEFAULT_IMAGE_SIZE)

    # Set a default position
    DEFAULT_IMAGE_TITLE_POSITION=(0,0)
    DEFAULT_IMAGE_POSITION1 = (0, 100)
    DEFAULT_IMAGE_POSITION2 = (width/2, 100)
    DEFAULT_IMAGE_POSITION3 = (0, (width/2)+100)
    DEFAULT_IMAGE_POSITION4 = (width/2, (width/2)+100)

    # Prepare loop condition
    running = False
    # Event loop
    while not running:
        # Close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True

            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_1:
                    currentLab=1
                    WIN1 = pygame.display.set_mode((WIDTH, WIDTH))
                    pygame.display.set_caption("A* Path Finding Algorithm")
                    main(WIN1, WIDTH,currentLab)
                    WIN2 = pygame.display.set_mode((WIDTH, WIDTH))
                    pygame.display.set_caption("Dijkstra's Path Finding Algorithm")
                    main2(WIN2, WIDTH, currentLab)
                    print("1")
                    running=True
                elif event.key ==pygame.K_2:
                    currentLab=2
                    WIN1 = pygame.display.set_mode((WIDTH, WIDTH))
                    pygame.display.set_caption("A* Path Finding Algorithm")
                    main(WIN1, WIDTH,currentLab)
                    WIN2 = pygame.display.set_mode((WIDTH, WIDTH))
                    pygame.display.set_caption("Dijkstra's Path Finding Algorithm")
                    main2(WIN2, WIDTH, currentLab)
                    print("2")
                    running=True
                elif event.key ==pygame.K_3:
                    currentLab=3
                    WIN1 = pygame.display.set_mode((WIDTH, WIDTH))
                    pygame.display.set_caption("A* Path Finding Algorithm")
                    main(WIN1, WIDTH,currentLab)
                    WIN2 = pygame.display.set_mode((WIDTH, WIDTH))
                    pygame.display.set_caption("Dijkstra's Path Finding Algorithm")
                    main2(WIN2, WIDTH, currentLab)
                    print("3")
                    running=True
                elif event.key ==pygame.K_4:
                    currentLab=4
                    WIN1 = pygame.display.set_mode((WIDTH, WIDTH))
                    pygame.display.set_caption("A* Path Finding Algorithm")
                    main(WIN1, WIDTH,currentLab)
                    WIN2 = pygame.display.set_mode((WIDTH, WIDTH))
                    pygame.display.set_caption("Dijkstra's Path Finding Algorithm")
                    main2(WIN2, WIDTH, currentLab)
                    print("4")
                    running=True


        # Background Color
        screen.fill((0, 0, 0))

        # Show the image
        screen.blit(titlePNG,DEFAULT_IMAGE_TITLE_POSITION)
        screen.blit(image1, DEFAULT_IMAGE_POSITION1)
        screen.blit(image2, DEFAULT_IMAGE_POSITION2)
        screen.blit(image3, DEFAULT_IMAGE_POSITION3)
        screen.blit(image4, DEFAULT_IMAGE_POSITION4)

        # Part of event loop
        pygame.display.flip()
    pygame.quit()

def main(win, width,currentLab):
    ROWS =50
    grid = make_grid(ROWS, width)

    rootNode=None
    goalNode=None

    run = True
    started = False #started
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if currentLab==1:
                for line in fBarriers1AStar:
                    fields=line.split(',')
                    field1=int(fields[0])
                    field2=int(fields[1])
                    row,col=(field1,field2)
                    spot = grid[row][col]  # index row/col in grid
                    spot.generateBarrierColor()
                    rootX,rootY=30,30
                    goalX,goalY=1,1
                tempNode = grid[rootX][rootY]
                rootNode = tempNode
                # rootNode.color=ORANGE
                rootNode.rootNodeColor()
                tempNode = grid[goalX][goalY]
                goalNode = tempNode
                # goalNode.color=TURQUOISE
                goalNode.goalNodeColor()

                if event.type == pygame.KEYDOWN:
                    startTime = time.time()
                    if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
                        for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
                            for node in row:  # then for the spots in that row, update all of our neighbors
                                node.updateAdjacentNodes(grid)
                        AStarAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)

                    print("totalTime: ", time.time()-startTime,"seconds")


            elif currentLab == 2:
                for line in fBarriers2AStar:
                    fields = line.split(',')
                    field1 = int(fields[0])
                    field2 = int(fields[1])
                    row, col = (field1, field2)
                    spot = grid[row][col]  # index row/col in grid
                    spot.generateBarrierColor()
                    rootX,rootY=24,22
                    goalX, goalY = 4,30

                tempNode = grid[rootX][rootY]
                rootNode = tempNode
                # rootNode.color=ORANGE
                rootNode.rootNodeColor()
                tempNode = grid[goalX][goalY]
                goalNode = tempNode
                # goalNode.color=TURQUOISE
                goalNode.goalNodeColor()

                if event.type == pygame.KEYDOWN:
                    startTime = time.time()
                    if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
                        for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
                            for node in row:  # then for the spots in that row, update all of our neighbors
                                node.updateAdjacentNodes(grid)
                        AStarAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)

                    print("totalTime: ", time.time() - startTime, "seconds")

            elif currentLab == 3:
                for line in fBarriers3AStar:
                    fields = line.split(',')
                    field1 = int(fields[0])
                    field2 = int(fields[1])
                    row, col = (field1, field2)
                    spot = grid[row][col]  # index row/col in grid
                    spot.generateBarrierColor()
                    rootX,rootY=3,5
                    goalX, goalY = 45,47

                tempNode = grid[rootX][rootY]
                rootNode = tempNode
                # rootNode.color=ORANGE
                rootNode.rootNodeColor()
                tempNode = grid[goalX][goalY]
                goalNode = tempNode
                # goalNode.color=TURQUOISE
                goalNode.goalNodeColor()

                if event.type == pygame.KEYDOWN:
                    startTime = time.time()
                    if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
                        for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
                            for node in row:  # then for the spots in that row, update all of our neighbors
                                node.updateAdjacentNodes(grid)
                        AStarAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)

                    print("totalTime: ", time.time() - startTime, "seconds")

            elif currentLab == 4:
                for line in fBarriers4AStar:
                    fields = line.split(',')
                    field1 = int(fields[0])
                    field2 = int(fields[1])
                    row, col = (field1, field2)
                    spot = grid[row][col]  # index row/col in grid
                    spot.generateBarrierColor()
                    rootX, rootY = 42, 26
                    goalX, goalY = 6, 44

                #rootX,rootY=30,30
                # rootX,rootY=24,22
                # rootX,rootY=3,5
                # rootX, rootY = 42, 26
                # print("root: ",rootX)
                # print("root: ",rootY)
                # print("goal: ",goalY)
                # print("goal: ",goalY)
                #goalX,goalY=1,1
                # goalX, goalY = 4,30
                # goalX, goalY = 45,47
                # goalX, goalY = 6, 44

                tempNode=grid[rootX][rootY]
                rootNode=tempNode
                # rootNode.color=ORANGE
                rootNode.rootNodeColor()
                tempNode=grid[goalX][goalY]
                goalNode=tempNode
                # goalNode.color=TURQUOISE
                goalNode.goalNodeColor()

                if event.type == pygame.KEYDOWN:
                    startTime = time.time()
                    if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
                        for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
                            for node in row:  # then for the spots in that row, update all of our neighbors
                                node.updateAdjacentNodes(grid)
                        AStarAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)

                    print("totalTime: ", time.time() - startTime, "seconds")


    pygame.quit()

# WIDTHMenu = 800
# WINMenu = pygame.display.set_mode((2706,WIDTHMenu))
# main0(WINMenu,WIDTHMenu)

#--
# menu()

# WIN1= pygame.display.set_mode((WIDTH,WIDTH))
# pygame.display.set_caption("A* Path Finding Algorithm")
# main(WIN1,WIDTH)

## ------------------------ DJAKSTRA'S ALGORITHM CALL ------------------------------------------------------
def main2(win, width,currentLab):
    ROWS = 50
    grid = make_grid(ROWS, width)

    rootNode = None
    goalNode = None

    run = True
    started = False  # started
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if currentLab == 1:
                for line in fBarriers1Dijkstra:
                    fields = line.split(',')
                    field1 = int(fields[0])
                    field2 = int(fields[1])
                    row, col = (field1, field2)
                    spot = grid[row][col]  # index row/col in grid
                    spot.generateBarrierColor()
                    rootX, rootY = 30, 30
                    goalX, goalY = 1, 1
                tempNode = grid[rootX][rootY]
                rootNode = tempNode
                # rootNode.color=ORANGE
                rootNode.rootNodeColor()
                tempNode = grid[goalX][goalY]
                goalNode = tempNode
                # goalNode.color=TURQUOISE
                goalNode.goalNodeColor()

                if event.type == pygame.KEYDOWN:
                    startTime = time.time()
                    if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
                        for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
                            for node in row:  # then for the spots in that row, update all of our neighbors
                                node.updateAdjacentNodes(grid)
                        DijstrasAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)

                    print("totalTime: ", time.time() - startTime, "seconds")



            elif currentLab == 2:
                for line in fBarriers2Dijkstra:
                    fields = line.split(',')
                    field1 = int(fields[0])
                    field2 = int(fields[1])
                    row, col = (field1, field2)
                    spot = grid[row][col]  # index row/col in grid
                    spot.generateBarrierColor()
                    rootX, rootY = 24, 22
                    goalX, goalY = 4, 30

                tempNode = grid[rootX][rootY]
                rootNode = tempNode
                # rootNode.color=ORANGE
                rootNode.rootNodeColor()
                tempNode = grid[goalX][goalY]
                goalNode = tempNode
                # goalNode.color=TURQUOISE
                goalNode.goalNodeColor()

                if event.type == pygame.KEYDOWN:
                    startTime = time.time()
                    if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
                        for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
                            for node in row:  # then for the spots in that row, update all of our neighbors
                                node.updateAdjacentNodes(grid)
                        DijstrasAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)

                    print("totalTime: ", time.time() - startTime, "seconds")

            elif currentLab == 3:
                for line in fBarriers3Dijkstra:
                    fields = line.split(',')
                    field1 = int(fields[0])
                    field2 = int(fields[1])
                    row, col = (field1, field2)
                    spot = grid[row][col]  # index row/col in grid
                    spot.generateBarrierColor()
                    rootX, rootY = 3, 5
                    goalX, goalY = 45, 47

                tempNode = grid[rootX][rootY]
                rootNode = tempNode
                # rootNode.color=ORANGE
                rootNode.rootNodeColor()
                tempNode = grid[goalX][goalY]
                goalNode = tempNode
                # goalNode.color=TURQUOISE
                goalNode.goalNodeColor()

                if event.type == pygame.KEYDOWN:
                    startTime = time.time()
                    if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
                        for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
                            for node in row:  # then for the spots in that row, update all of our neighbors
                                node.updateAdjacentNodes(grid)
                        DijstrasAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)

                    print("totalTime: ", time.time() - startTime, "seconds")

            elif currentLab == 4:
                for line in fBarriers4Dijkstra:
                    fields = line.split(',')
                    field1 = int(fields[0])
                    field2 = int(fields[1])
                    row, col = (field1, field2)
                    spot = grid[row][col]  # index row/col in grid
                    spot.generateBarrierColor()
                    rootX, rootY = 42, 26
                    goalX, goalY = 6, 44

                tempNode = grid[rootX][rootY]
                rootNode = tempNode
                # rootNode.color=ORANGE
                rootNode.rootNodeColor()
                tempNode = grid[goalX][goalY]
                goalNode = tempNode
                # goalNode.color=TURQUOISE
                goalNode.goalNodeColor()

                if event.type == pygame.KEYDOWN:
                    startTime = time.time()
                    if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
                        for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
                            for node in row:  # then for the spots in that row, update all of our neighbors
                                node.updateAdjacentNodes(grid)
                        DijstrasAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)

                    print("totalTime: ", time.time() - startTime, "seconds")

    pygame.quit()
    # ROWS =50
    # grid = make_grid(ROWS, width)
    #
    # run = True
    # started = False
    # while run:
    #     draw(win, grid, ROWS, width)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
    #         if started:
    #             continue
    #         if currentLab==1:
    #             for line in fBarriers1Dijkstra:
    #                 fields=line.split(',')
    #                 field1=int(fields[0])
    #                 field2=int(fields[1])
    #                 row,col=(field1,field2)
    #                 spot = grid[row][col]  # index row/col in grid
    #                 spot.generateBarrierColor()
    #                 rootX,rootY=30,30
    #                 goalX,goalY=1,1
    #
    #             tempNode = grid[rootX][rootY]
    #             rootNode = tempNode
    #             # rootNode.color=ORANGE
    #             rootNode.rootNodeColor()
    #             tempNode = grid[goalX][goalY]
    #             goalNode = tempNode
    #             # goalNode.color=TURQUOISE
    #             goalNode.goalNodeColor()
    #
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
    #                     for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
    #                         for node in row:  # then for the spots in that row, update all of our neighbors
    #                             node.update_neighbors(grid)
    #
    #                     DijstrasAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)
    #         if currentLab == 2:
    #             for line in fBarriers2Dijkstra:
    #                 fields = line.split(',')
    #                 field1 = int(fields[0])
    #                 field2 = int(fields[1])
    #                 row, col = (field1, field2)
    #                 spot = grid[row][col]  # index row/col in grid
    #                 spot.generateBarrierColor()
    #                 rootX,rootY=24,22
    #                 goalX, goalY = 4,30
    #
    #             tempNode = grid[rootX][rootY]
    #             rootNode = tempNode
    #             # rootNode.color=ORANGE
    #             rootNode.rootNodeColor()
    #             tempNode = grid[goalX][goalY]
    #             goalNode = tempNode
    #             # goalNode.color=TURQUOISE
    #             goalNode.goalNodeColor()
    #
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
    #                     for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
    #                         for node in row:  # then for the spots in that row, update all of our neighbors
    #                             node.update_neighbors(grid)
    #
    #                     DijstrasAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)
    #         if currentLab == 3:
    #             for line in fBarriers3Dijkstra:
    #                 fields = line.split(',')
    #                 field1 = int(fields[0])
    #                 field2 = int(fields[1])
    #                 row, col = (field1, field2)
    #                 spot = grid[row][col]  # index row/col in grid
    #                 spot.generateBarrierColor()
    #                 rootX,rootY=3,5
    #                 goalX, goalY = 45,47
    #
    #             tempNode = grid[rootX][rootY]
    #             rootNode = tempNode
    #             # rootNode.color=ORANGE
    #             rootNode.rootNodeColor()
    #             tempNode = grid[goalX][goalY]
    #             goalNode = tempNode
    #             # goalNode.color=TURQUOISE
    #             goalNode.goalNodeColor()
    #
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
    #                     for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
    #                         for node in row:  # then for the spots in that row, update all of our neighbors
    #                             node.update_neighbors(grid)
    #
    #                     DijstrasAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)
    #         if currentLab == 4:
    #             for line in fBarriers4Dijkstra:
    #                 fields = line.split(',')
    #                 field1 = int(fields[0])
    #                 field2 = int(fields[1])
    #                 row, col = (field1, field2)
    #                 spot = grid[row][col]  # index row/col in grid
    #                 spot.generateBarrierColor()
    #                 rootX, rootY = 42, 26
    #                 goalX, goalY = 6, 44
    #
    #             #rootX,rootY=30,30
    #             # rootX,rootY=24,22
    #             # rootX,rootY=3,5
    #             # rootX, rootY = 42, 26
    #
    #
    #             #goalX,goalY=1,1
    #             # goalX, goalY = 4,30
    #             # goalX, goalY = 45,47
    #             # goalX, goalY = 6, 44
    #
    #             tempNode=grid[rootX][rootY]
    #             rootNode=tempNode
    #             # rootNode.color=ORANGE
    #             rootNode.rootNodeColor()
    #             tempNode=grid[goalX][goalY]
    #             goalNode=tempNode
    #             # goalNode.color=TURQUOISE
    #             goalNode.goalNodeColor()
    #         # for line in fBarriers1Dijkstra:
    #         #     fields=line.split(',')
    #         #     field1=int(fields[0])
    #         #     field2=int(fields[1])
    #         #     row,col=(field1,field2)
    #         #     spot = grid[row][col]  # index row/col in grid
    #         #     spot.generateBarrierColor()
    #         #
    #         # rootX, rootY = 30, 30
    #         # goalX, goalY = 1, 1
    #         # tempNode = grid[rootX][rootY]
    #         # rootNode = tempNode
    #         # # rootNode.color=ORANGE
    #         # rootNode.rootNodeColor()
    #         # tempNode = grid[goalX][goalY]
    #         # goalNode = tempNode
    #         # # goalNode.color=TURQUOISE
    #         # goalNode.goalNodeColor()
    #
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_SPACE and rootNode and goalNode:  # if we have a start node we are good to go     #did we press a keyboard down?? and not
    #                 for row in grid:  # if we press the key down and the key is the spacebar and we have not started the algorithm
    #                     for node in row:  # then for the spots in that row, update all of our neighbors
    #                         node.update_neighbors(grid)
    #
    #                 DijstrasAlg(lambda: draw(win, grid, ROWS, width), grid, rootNode, goalNode)
    #
    # pygame.quit()

menu()

