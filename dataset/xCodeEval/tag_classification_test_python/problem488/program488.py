def program488():
    import sys
    z=list(map(int,input().split()))
    x=list(map(str,input()))
    c=[i for i in range(z[0]) if x[i]=='T'or x[i]=='G']
    for i in range(min(c)+z[1],z[0],z[1]):
        if x[i]=='G'or x[i]=='T':
            print('YES')        
            sys.exit(0)
        if x[i]=='#':
              break              
    print('NO')