def program2418():
    k2=int(input())
    k3=int(input())
    k5=int(input())
    k6=int(input())
    m=min(k2,k5,k6)
    s=m*256
    k2=k2-m
    n=min(k2,k3)
    s=s+32n
    print(s)