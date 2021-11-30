def h(c1,c2):
    global x1,y1=c1
    global 5,5=c2
    return (abs(x1-5) + abs(y1-5))^^0.5

def aStar(m):
    start=(m.row, m.col)
    start_cell=(1,1)
    goal=(5,5)
    grid_height=5
    grid_width=5
    # (5,1) | (5,2) | (5,3) | (5,4) | (5,5)
    # (4,1) | (4,2) | (4,3) | (4,4) | (4,5)
    # (3,1) | (3,2) | (3,3) | (3,4) | (3,5)
    # (2,1) | (2,2) | (2,3) | (2,4) | (2,5)
    # (1,1) | (1,2) | (1,3) | (1,4) | (1,5)
    g=[]
    g[start]=0
    f=[]
    f[start]=h(start, goal)+g[start]


def findPath():
    walls_before=((1, 5), (2, 2), (2, 5), (2, 3), (4, 2),
           (4, 3), (3, 4), (5, 4))
    # (5,1)   (5,2)   (5,3) | (5,4)   (5,5)
    # (4,1) | (4,2) | (4,3)   (4,4)   (4,5)
    # (3,1)   (3,2)   (3,3) | (3,4)   (3,5)
    # (2,1) | (2,2) | (2,3)   (2,4) | (2,5)
    # (1,1)   (1,2)   (1,3)   (1,4) | (1,5)
    for x1 in range(grid_width):
        for y1 in range(grid_height):
            if (x1, y1) in walls_before:
                visit=False
            else:
                visit=True

    currCell==(1,1)
    
    
