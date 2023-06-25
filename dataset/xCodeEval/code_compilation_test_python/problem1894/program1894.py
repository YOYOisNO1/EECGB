def program1894():
    n=int(input())
    m=[[1]*n,[1]*n]
    while n-1>=0:
        a=n%2;b=(n-1)%2;
        for i in xrange(1,n):
            for j in xrange(n):
                m[b][j]+=m[a][i]
        n--
    print m[0][n-1]