def program1568():
    n,p,k=map(int,input().split())
    ans=" ({}) ".format(p)
    x=""
    for i in range(max(p-k,1),p):x+=" {}".format(i)
    ans=x+ans
    for i in range(p+1,min(n+1,p+k+1)):ans+="{} ".format(i)
    if p+k<n :ans+=">>"
    if p-k>1 :ans="<<"+ans
    print(ans)