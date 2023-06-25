def program3639():
    
    n , u = map(int,input().split())
    
    
    s = input()
    t = input()
    inf = 10**12
    
    
    if t[0]==t[1]:
    
        u = min(n, s.count(t[0])+u)
        print((u-1)*u//2)
    else:
        l =[ [   [-inf]*(u+1 ) for i in range(n+1)] for j in range(n+1)]
    
        l[0][0][0] = 0
    
        for  i in range(n):
        
            for j in range(n+1):
    
                for k in  range(u+1):
    
    
                    if s[i]==t[0]:
    
                        if j+1 <=n:
    
                            l[i+1][j+1][k]= max( l[i+1][j+1][k], l[i][j][k]  )
                    elif s[i]==t[1]:
    
                        l[i+1][j][k] = max( l[i+1][j][k] , l[i][j][k]+j)
                    else:
                        l[i+1][j][k]= max(l[i+1][j][k],l[i][j][k])
    
                    if k+1 <= u and j+1<=n:
    
                        l[i+1][j+1][k+1]= max(l[i+1][j+1][k+1],l[i][j][k])
    
                    if k+1 <= u:
    
                        l[i+1][j][k+1] = max(l[i+1][j][k+1], l[i][j][k]+j)
        ans = -inf
        for j in range(n+1):
            for k in range(u+1):
    
                ans = max(ans, l[-1][j][k])
    
        print(ans)
    
    
    
    
        