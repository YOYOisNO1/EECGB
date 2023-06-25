def program1688():
    import sys
    
    hulp=sys.stdin.readline().split()
    
    n,m=int(hulp[0]),int(hulp[1])
    
    f=[int(x) for x in sys.stdin.readline().split()]
    
    f.sort()
    mindif=1000
    
    for x in range(m-n+1):
        mindif=min(f[x+n-1]-f[x],mindif)
    
    
    
    print mindif