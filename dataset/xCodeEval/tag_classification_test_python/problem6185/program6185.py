def program6185():
    """http://codeforces.com/contest/370/problem/0"""
    
    r1,c1,r2,c2 = map(int,input().split())
    #print(r1,c1,r2,c2)
    rook = (0 if r1 == r2 else 1)+(0 if c1 == c2 else 1)
    bishop = (1 if abs(c1-c2) == abs(r1-r2) else 2) if (abs(r1-r2)+abs(c1-c2))%2==0 else 0
    king = max(abs(r1-r2),abs(c1-c2))
    print(rook,) bishop, king