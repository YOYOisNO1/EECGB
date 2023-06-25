def program6153():
    import sys
    
    s = sys.stdin.readline().split()
    r1 = int(s[0])
    c1 = int(s[1])
    r2 = int(s[2])
    c2 = int(s[3])
    
    korol = max(abs(r1-r2),abs(c1-c2))
    
    ladya = 2
    if r1==r2 or c1==c2:
        ladya = 1
        
        
    r20 = r2-r1
    c20 = c2-c1
    
    if ((r1+c1)%2) != ((r2+c2)%2):
        slon = 0
    elif abs(r20) == abs(c20):
        slon = 1
    else:
        slon = 2
    
    print(ladya,) slon, korol