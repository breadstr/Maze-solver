maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0]
]


def solveMaze(maze,vertical,horizontal):
    #need number of items in each list and total amount of lists
    #number of items in a list
    numItem = len(maze[0])-1
    #number of total lists
    numList = len(maze)-1
    #print(numList)


    #base cases
    #if vertical or horizontal are out of index range
    if vertical < 0 or vertical > numList or horizontal < 0 or horizontal > numItem:
        return False

    #if vertical or horizontal are out of index range or are in an already visited place
    if maze[vertical][horizontal] == 1 or maze[vertical][horizontal] == 3:
        return False

    #check if vertical and horizontal are in the bottom right corner of the list
    if vertical == numList and horizontal == numItem:
        maze[vertical][horizontal] = 3
        return True

    #mark maze[vertical][horizontal] to 3 to show it is visited
    maze[vertical][horizontal] = 3

    print("ver", vertical)
    print("ho", horizontal)
    print(maze)

    #recusive cases
    #search every direction
    if solveMaze(maze,vertical+1,horizontal):
        return True
    if solveMaze(maze,vertical-1, horizontal):
        return True
    if solveMaze(maze,vertical, horizontal+1):
        return True
    if solveMaze(maze,vertical, horizontal-1):
        return True

    return False

q =solveMaze(maze,0,0)
print(q)
for line in maze:
    print(line)