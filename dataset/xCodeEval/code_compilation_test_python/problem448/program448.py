def program448():
    n,k=input().split()
    n,k=int(n),int(k)
    a=list(map(int,input().split()))
    p=(2*k-1)*n-2*sum(a)
    if p<0:
        print(0)
    else
        print(p)