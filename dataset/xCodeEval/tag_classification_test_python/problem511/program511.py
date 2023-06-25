    import fileinput
def D(a):print(a)
def S(s,I):return int(s.split(" ")[I])
def dyn(u,r):
        global N
        global X
        global dp
        if(u<0):return 0
        if(r==0):return 1
        if(u>=N):return 0
        if(dp[u][r]!=-1):return dp[u][r];
        v=0
        for i in range(26):
            v+=dyn(X[u][i]+1,r-1)
        dp[u][r]=v
        return v
def main():
        z=0
        global N
        global X
        global dp
        K=0
        for l in fileinput.input():
            z+=1
            if(z<2):
                N=S(l,0)
                K=S(l,1)
                continue
            X=[0]*(N+1)
            X[N]=[-666]*26
            for i in xrange(N-1,-1,-1):
                X[i]=[-1]*26
                for j in range(26):X[i][j]=X[i+1][j]
                X[i][ord(l[i])-97]=i
            dp=[0]*N
            for i in range(N):
                dp[i]=[-1]*(N+1)
        o=0
        for i in xrange(N,-1,-1):
            a=dyn(0,i)
            if(a<=K):
                o+=(N-i)*a
                K-=a
            else:
                o+=(N-i)*K
                K=0
        if(K!=0):D(-1)
        else: D(o)
    main()