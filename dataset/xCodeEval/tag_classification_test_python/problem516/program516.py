def program516():
    n,m,a=map(int,input().split())
    l=int(n/a)
    x=int(m/a)
    if(n%a!=0):
        l=l+1
    if(m%a!=0):
        x=x+1
    print(l*x)