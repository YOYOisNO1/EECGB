    import math
    side = "abcdefgh"
def intoPos(inp):
        txt = [c for c in inp]
        txt[0] = side.index(txt[0])
        txt[1] = int(txt[1]) - 1
        return txt
    
    r = intoPos(input())
    k = intoPos(input())
    
def possible(x, y):
        if x == k[0] and y == k[1]:
            return False
    
    def towerView(x, y, r, r1):
            if x == r:
                    return True
            return False
    
        if towerView(x, y, r[0], r[1]) or towerView(y, x, r[1], r[0]):
            return False
    
    def knightView(x, y, ax, ay):
            for x1 in range(-2, 3):
                for y1 in range(-2, 3):
                    if math.abs(x1) != math.abs(y1) and x1 != 0 and y1 != 0:
                        if ax + x1 == x and ay + y1 == y:
                            return True
            return False
    
        if knightView(x, y, r[0], r[1]) or knightView(x, y, k[0], k[1]):
            return False
    
        return True
    
    sum = 0
    for x in range(8):
        for y in range(8):
            if possible(x, y):
                sum += 1
    
    print(sum)