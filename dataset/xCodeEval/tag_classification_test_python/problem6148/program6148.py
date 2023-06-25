def solve():
        r1,c1,r2,c2 = map(int, input().split())
        rook = bishop = king = 0
        if r1 == r2 and c1 == c2:
            print(rook,bishop,king)
            return
        A = [[None for i in range(8)] for i in range(8)]
        cur = 1
        nex = 0
        for i in range(8):
            for j in range(8):
                A[i][j] = cur
                t = cur
                cur = nex
                nex = t
            t = cur
            cur = nex
            nex = t
        if r1 == r2 or c1 == c2:
            rook = 1
        else:
            rook = 2
    
        king = max(abs(r1-r2), abs(c1-c2))
    
        if A[r1-1][c1-1] == A[r2-1][c2-1]:
            # diagonal?
            found = False
            step = 1
            while not found and step <= 8:
                if r1 + step == r2 and c1 + step == c2 or \
                    r1 - step == r2 and c1 + step == c2 or \
                    r1 + step == r2 and c1 - step == c2 or \
                    r1 - step == r2 and c1 - step == c2:
                    bishop = 1
                    found = True
                step += 1
            if not found:
                bishop = 2
        else:
            bishop = 0
    
        print(rook,bishop,king)
    
    solve()