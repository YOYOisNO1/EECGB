def program3314():
    n,m,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    s=min(l1)
    d=k//s
    c=k%s
    b=max(l2)
    c+=d*b
    if(c>k):
        print(c)
    else:
        print(k)