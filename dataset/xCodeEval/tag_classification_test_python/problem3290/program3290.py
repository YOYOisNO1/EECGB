def program3290():
    import math
    n=int(input())
    a=int(math.sqrt(n))
    while n%a !=0:
        a=a-1
    print(a,n//a)