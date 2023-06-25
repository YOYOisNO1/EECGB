def program5259():
    n,m,k=map(int,input().split())
    if n<k or k==1:r=n
    elif n==k:r=-~k/2
    else:r=1+k%2
    print(m**r%(10**9+7))
    