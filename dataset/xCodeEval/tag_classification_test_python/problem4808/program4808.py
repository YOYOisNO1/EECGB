def program4808():
    import math
    n=input()
    x=math.trunc(math.sqrt(n))
    if n-x*x==0:
        print(4*x)
    else:
        if n-x*x<=x:
            print(2*x+2*(x+1))
        else:
            print(4*x+4)