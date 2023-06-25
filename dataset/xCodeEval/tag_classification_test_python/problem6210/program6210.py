def ladya(r1, c1, r2, c2):
        if r1 - r2 == 0 or c1 - c2 == 0:
            return 1
        else:
            return 2
    
def slon(r1, c1, r2, c2):
        if (r1 + c1)%2 == (r2 + c2)%2:
            if abs(r2 - r1) == abs(c2-c1):
                return 1
            else:
                return 2
        else:
            return 0
    
def king(r1, c1, r2, c2):
        return max(abs(r1 - r2), abs(c1 - c2))
    
    inp = input().split()
    r1 = int(inp[0])
    c1 = int(inp[1])
    r2 = int(inp[2])
    c2 = int(inp[3])
    print(ladya(r1,) c1, r2, c2), slon(r1, c1, r2, c2), king(r1, c1, r2, c2)