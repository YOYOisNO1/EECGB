    from sys import stdin
    s=stdin.readline().strip()
    k=int(stdin.readline().strip())
    n=len(s)
    dp=[[[[[ None for ty in range(2)]for tt in range(2)]for i in range(2)] for j in range(k+1)] for k1 in range(n)]
def minn(a,b):
        if a<b:
            return a
        return b
def maxx(a,b):
        if a>b:
            return a
        return b
def sol(i,j,t,c,mt):
        if i==n:
            if j!=0:
                if mt:
                    return -10001
                else:
                    return 10001
            else:
                return 0
        if dp[i][j][t][c][mt]!=None:
            return dp[i][j][t][c][mt]
        ans=0
        if c==-1:
            c=(s[i]=="F")
        if c:
            if t:
                ans=-1+sol(i+1,j,t,-1,mt)
            else:
                ans=1+sol(i+1,j,t,-1,mt)
            if j>0:
                if mt:
                    ans=maxx(ans,sol(i,j-1, t,0,mt))
                else:
                    ans=minn(ans,sol(i,j-1, t,0,mt))       
        else :
            ans=sol(i+1,j,not t,-1,mt)
            if j>0:
                if mt:
                    ans=maxx(ans,sol(i,j-1, t,1,mt))
                else:
                    ans=minn(ans,sol(i,j-1, t,1,mt))
        dp[i][j][t][c][mt]=ans
        return dp[i][j][t][c][mt]
    print(max(-sol(0,k,0,-1,0),sol(0,k,0,-1,1)))
                    
                    