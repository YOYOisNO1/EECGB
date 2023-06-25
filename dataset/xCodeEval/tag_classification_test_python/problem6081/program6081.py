def program6081():
    import math
    F=lambda x:math.factorial(x)
    n,w,b=map(int,input().split())
    print((F(w)*F(b)*(w-1)*F(w+b-3)/F(n-3)/F(w+b-n))%1000000009)
    