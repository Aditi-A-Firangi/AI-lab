class Node:
    def __init__(self, state, level):
        self.grid = state
        self.level = level
        self.cost = 0

def G(state):
    return state.level

def H(state, target):
    grid = state.grid
    dist = 0
    for i in grid:
        d1, d2 = grid.index(i), target.index(i)
        x1, y1 = d1 % 3, d1 // 3
        x2, y2 = d2 % 3, d2 // 3
        dist += abs(x1-x2) + abs(y1-y2)
    return dist

def F(state, target):
    return G(state) + H(state, target)

def printGrid(state):
    state = state.grid.copy()
    state[state.index(0)] = ' '
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()

def inFrontier(frontier, neighbour):
    return len([state for state in frontier if state.grid == neighbour.grid]) > 0

def astar(state, target):
    frontier = [Node(state, 1)]
    
    while frontier:
        frontier.sort(key = lambda x: x.cost)
        state = frontier.pop(0)
        print(f'Level: {state.level}')
        printGrid(state)
        
        if state.grid == target:
            print(f"Puzzle solved! ")
            return
        
        neighbours = possible_moves(state)
        for neighbour in neighbours:
            neighbour = Node(neighbour, state.level + 1)
            neighbour.cost = F(neighbour, target)
            if not inFrontier(frontier, neighbour):
                frontier.append(neighbour)
    
    print("Can't solve puzzle! ")

def possible_moves(state):
    b = state.grid.index(0)  
    d = []
    if b not in [0,1,2]: 
        d += 'u'
    if b not in [6,7,8]:
        d += 'd'
    if b not in [2,5,8]: 
        d += 'r'
    if b not in [0,3,6]: 
        d += 'l'
    pos_moves = []
    for move in d:
        pos_moves.append(gen(state,move,b))
    return pos_moves

def gen(state, move, blank):
    temp = state.grid.copy()                              
    if move == 'u':
        temp[blank-3], temp[blank] = temp[blank], temp[blank-3]
    elif move == 'd':
        temp[blank+3], temp[blank] = temp[blank], temp[blank+3]
    elif move == 'r':
        temp[blank+1], temp[blank] = temp[blank], temp[blank+1]
    elif move == 'l':
        temp[blank-1], temp[blank] = temp[blank], temp[blank-1]
    return temp


src = [1,2,3,4,0,6,7,5,8]
target = [1,2,3,4,5,6,7,8,0]         
       
astar(src, target)
