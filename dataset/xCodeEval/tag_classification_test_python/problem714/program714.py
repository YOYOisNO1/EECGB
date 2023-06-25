def program714():
    n,l,r=[int(x) for x in input().split()]
    x=int((2**l)-1+(n-l))
    print(x,end=" ")
    x=int((2**r)-1)
    y=int((n-r)*(2**(r-1)))
    z=x+y
    print(f"{z}")