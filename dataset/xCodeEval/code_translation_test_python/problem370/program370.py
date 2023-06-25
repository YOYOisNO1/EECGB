def program370():
    n,k=[int(s) for s in input().split()]
    a=[int(s) for s in input().split()]
    m=2*(n*k-sum(a))-n
    print(m if m>0 else 0)