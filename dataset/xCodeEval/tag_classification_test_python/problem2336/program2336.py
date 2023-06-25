def program2336():
    m,n = map(int,input().strip().split())
    
    a = []
    for i in xrange(m):
        a.append(input().strip())
    xx = [-1,0,1,0]
    yy = [0,1,0,-1]
    res = 0
    for i in xrange(m):
        for j in xrange(n):
            if a[i][j] == 'W':
                for k in xrange(4):
                    u = i+xx[k]
                    v = j+yy[k]
                    if (u>=0 and v>=0 and u<m and v<n and a[u][v]=='P'):
                        res+=1
                        break
                      
    print(res)
    
            