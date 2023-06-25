def program4879():
    n,k=list(map(int,input().split()))
    if k%n==0 and k//n==2:
        print(n)
    elif k%n!=0 and k//n==2:
        a=k-2*n
        print(n-a)
    else:
        print(0)
        