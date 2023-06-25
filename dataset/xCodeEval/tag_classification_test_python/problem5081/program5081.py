def gank(n,A,b,c,d):
        a = [0]*4
        a[0] = A+b
        a[1] = A+c
        a[2] = b+d
        a[3] = c+d
        mi = 1e9
        ma = 0
        for i in range(4):
            ma = max(ma,a[i])
            mi = min(mi,a[i])
        if(1 + 1 + ma > 1+n+mi):
            return 0
        x = ma - mi + 1
        y = n - x + 1
        return y*n
    
    
    n,a,b,c,d = map(int , input().split(' '))
    print(gank(n,a,b,c,d))