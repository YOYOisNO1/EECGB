    input()
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    a[1], a[2] = a[2], a[1]
    b[1], b[2] = b[2], b[1]
    
    maxwin = min(a[0], b[2]) + min(a[1], b[0]) + min(a[2], b[1])
    
def calc(a, b, left):
        m = 10**9
        for possible in left[:]:
            newleft, newa, newb = left[:], a[:], b[:]
            newleft.remove(possible)
            
            played = min(a[possible[0]], b[possible[1]] )
            newa[possible[0]] -= played
            newb[possible[1]] -= played
            res = calc(newa, newb, newleft)
            m = min(m, res)
        if not len(left):
            return min(a[0], b[2]) + min(a[1], b[0]) + min(a[2], b[1])
    
        return m
    
    minwin = calc(a[:], b[:], [(0,0), (0,1), (1,1), (1,2), (2,0), (2,2)] )
    
    print((minwin,) maxwin)