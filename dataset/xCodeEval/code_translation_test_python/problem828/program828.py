def program828():
    n,k=[int(f)for f in input().split()]
    a=(0 if n==k or k==0 else 1)
    b=(k*2 if n//3>=k else n-k)
    print(a,(b if k!=0 else 0))