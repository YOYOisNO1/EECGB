def program7641():
    a,b,p,x=map(int,input().split())
    ans=0
    for j in range(p-1):
        y=b*pow(pow(a,j,p),p-2,p)%p
        i=(j-y+p)%p
        t=i*(p-1)+j
        if(x-t>=0):
            ans+=((x-t)//(p*(p-1))+1)
    print(ans)        