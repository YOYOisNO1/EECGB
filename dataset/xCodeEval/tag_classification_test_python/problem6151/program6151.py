def program6151():
    r1,c1,r2,c2=map(int,input().split())
    ans=[0,0,0]
    if r1==r2 or c1==c2:
        ans[0]=1
    else:
        ans[0]=2
    if (r1+c1)%2==(r2+c2)%2:
        if (r1-c1)==(r2-c2) or (r1+c1)==(r2+c2):
            ans[1]=1
        else:
            ans[1]=2
    else:
        ans[1]=0
    ans[2]=max(abs(r1-r2),abs(c1-c2))
    for i in ans:
        print(i,)