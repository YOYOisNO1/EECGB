def program5238():
    n,m=map(int,input().split())
    ans=5*(n//5)*(m//5)
    p=n%5
    q=m%5
    tmp=0
    for i in range(1,p+1):
        for j in range(1,q+1):
            if (i+j)%5==0:
                tmp+=1
    res1,res2=0,0
    for i in range(1,p+1):
        for j in range(1,6):
            if (i+j)%5==0:
                res1+=1
    for i in range(1,q+1):
        for j in range(1,6):
            if(i+j)%5==0:
                res2+=1
    ans=ans+res1*(m//5)+res2*(n//5)+tmp
    print(ans) 