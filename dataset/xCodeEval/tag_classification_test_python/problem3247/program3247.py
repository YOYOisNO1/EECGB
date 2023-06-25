    from sys import stdin
    
    
def input():
        return stdin.readline()[:-1]
    
    
def intput():
        return int(input())
    
    
def sinput():
        return input().split()
    
    
def intsput():
        return map(int, sinput())
    
    
    debugging = False
def dprint(*args):
        if debugging:
            print(*args)
        else:
            pass
    
    
    
    # Code
    
    firstx, firsty, ax, ay, bx, by = intsput()
    
    startx, starty, t = intsput()
    
    
def next(prevx, prevy):
        return prevx * ax + bx, prevy * ay + by
    
    
def reachable(x, y):
        return x + y
    
    
def distance(start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])
    
    
    nodes = []
    curx, cury = firstx, firsty
    while True:
        if curx > 10 ** 17 or cury > 10 ** 17:
            break
        nodes.append((curx, cury))
        curx, cury = next(curx, cury)
    
    best = 0
    for firstreach in range(len(nodes)):
        for lastreach in range(len(nodes)):
            totaldist = distance(nodes[firstreach], (startx, starty)) + distance(nodes[firstreach], nodes[lastreach])
            #print(firstreach, 'to', lastreach, 'takes', totaldist)
            if totaldist <= t:
                best = max(abs(firstreach - lastreach) + 1, best)
    
    print(best)