def program1703():
    import math
    n,m=input().split(' ')
    m=int(m)
    n=int(n)
    if m==0:
        print(1)
    elif(m==n):
        print(0)
    else:
        print(min(n-m,m))