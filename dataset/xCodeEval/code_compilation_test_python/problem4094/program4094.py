    import sys
    
def switchOn(switchedOn, points):
        for (x,y) in points:
            if (x,y) not in switchedOn:
                switchedOn.add((x,y))
        
def getNeighbors(x,y):
        neighbors = []
        if x!=n:
            neighbors.append((x+1,y))
        if y!=n:
            neighbors.append((x,y+1))
        if x!=1:
            neighbors.append((x-1,y))
        if y!=1:
            neighbors.append((x,y-1))
        return neighbors
    
def expand(points,i,switchedOn,c):
        switchOn(switchedOn, points)
        if len(switchedOn) >= c:
            print i
            sys.exit()
        else:
            allNeighbors = []
            for (x,y) in points:            
                neighbors = getNeighbors(x,y) 
                allNeighbors.extend(neighbors)
            expand(allNeighbors,i+1,switchedOn,c)
    
    if __name__ == '__main__':
        n,x,y,c = map(int,input().split())
        if c == 1:
            print 0
        else:
            switchedOn = set()
            points = [(x,y)]
            expand(points,0,switchedOn,c)