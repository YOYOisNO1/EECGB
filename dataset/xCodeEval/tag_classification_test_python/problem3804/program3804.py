def program3804():
    import sys
    l=0
    for line in sys.stdin:
        if l == 0: xn,xb=map(int,line.split())
        if l == 1: xi=line.split()
        if l == 2: yn,yb=map(int,line.split())
        if l == 3: yi=line.split()
        l += 1
    
    x = 0
    i = xn-1
    p = 0
    while (i >= 0):
        x+=int(xi[p])*(xb**i)
        i-=1
        p+=1
    i = yn-1
    p = 0
    while (i >= 0):
        x-=int(yi[p])*(yb**i)
        i-=1
        p+=1
    if (x>0): print((">"))
    elif (x==0): print(("="))
    else: print(("<"))