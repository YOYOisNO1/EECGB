def program6176():
    from sys import stdin,stdout
    ii1 = lambda: int(stdin.readline())
    is1 = lambda: stdin.readline()
    iia = lambda : map(int, stdin.readline().split())
    isa = lambda: stdin.readline().split()
    
    r1, c1, r2, c2 = iia()
    ele = None
    if r1 == r2 or c1 == c2:
        ele = 1
    else:
        ele = 2
        
    king = None
    if r1 == r2:
        king = abs(c2 - c1)
    elif c1 == c2:
        king = abs(r2 - r1)
    elif abs(r2 - r1) == abs(c2 - c1):
        king = abs(r2 - r1)
    else:
        king = max(abs(r2 - r1), abs(c2 - c1))
    
    bishop = None
    
    if r1 == r2:
        if abs(c2 - c1) % 2 == 0:
            bishop = 2
        else:
            bishop = 0
    elif c1 == c2:
        if abs(r2 - r1) % 2 == 0:
            bishop = 2
        else:
            bishop = 0
    elif abs(r2 - r1) == abs(c2 - c1):
        bishop = 1
    elif (r1 + c1) % 2 != (r2 + c2) % 2:
        bishop = 0
    else:
        bishop = 2
    print(ele,bishop,king)
        