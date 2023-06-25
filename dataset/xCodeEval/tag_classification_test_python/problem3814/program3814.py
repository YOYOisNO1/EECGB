def program3814():
    n,d=map(int,input().split())
    a=map(int,input().split())
    m=int(input())
    s=0
    if(m>n):
        s=sum(a)-d*(m-n)
    if(m==n):
        s=sum(a)
    if(m<n):
        a=sorted(a)
        a=a[:m]
        s=sum(a)
    print(s)