def updiv(t,s):
        if t%s==0: return t/s
        else: return t/s+1
    
    n,m = map(int,input().split())
    if n>m: n,m=m,n
    
    ans=max(updiv(n,3)*m, updiv(m,3)*n)
    ans=max(ans,updiv(m*n,2))
    if n>=2 and m>=2: ans=max(ans,4)
    
    if n==2:
        s1=m/2
        s2=m-s1
        ans=max(ans,2*(updiv(s1,2)+updiv(s2,2)))
    
    print(ans)