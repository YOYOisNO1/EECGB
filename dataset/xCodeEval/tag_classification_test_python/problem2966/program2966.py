def program2966():
    l,r=map(int,input().split(" "))
    x=len(str(r))
    m='9'*x
    m=int(m)
    m1='1'+'0'*(x-1)
    m1=int(m1)
    ans=max(l*(m-l),r*(m-r))
    if l<=m1<=r:
        ans=max(ans,m1*(m-m1))
    
    if l<=m//2<=r:
        ans=max(ans,(m//2)*(m-m//2))
    
    if l<=m//2+1<=r:
        ans=max(ans,(m//2+1)*(m-m//2-1))
    
    print(ans)