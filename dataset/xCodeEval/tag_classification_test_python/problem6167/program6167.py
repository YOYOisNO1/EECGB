def move(r1, c1, r2, c2):
        if r2 == r1 or c2 == c1:
            l = 1
        else:
            l = 2
    
        k = max(abs(r2 - r1), abs(c2 - c1))
    
        if ((r1 + c1) % 2) == ((r2 + c2) % 2):
            if abs(r2 -r1) == abs(c2 - c1):
                s = 1
            else:
                s = 2
        else:
            s = 0
        return l, k, s
    
    r1, c1, r2, c2 = map(int, input().split())
    l, k, s = move(r1, c1, r2, c2)
    
    print(l, s, k)