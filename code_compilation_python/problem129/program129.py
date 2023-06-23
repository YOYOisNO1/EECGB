def program129():
    n,p,t=input().split()
    n=int(n)
    p=float(p)
    t=int(t)
    ans=0
    temp=t
    for i in range(1,n+1):
        #temp=t
        ans=ans+pow(p,i-1)*(1-pow(1-p,temp))
        temp=temp-1
        if temp==0:
            break
        #print ans,temp
    print ans