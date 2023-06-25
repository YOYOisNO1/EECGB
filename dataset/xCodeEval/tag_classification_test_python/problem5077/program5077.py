def program5077():
    import math
    n=int(input())
    if(n%2!=0):
        print(0)
    else:
        a=math.ceil(n/4)
        print(a-1)