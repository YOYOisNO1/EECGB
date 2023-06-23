def f(a,b,c):
        if a==b:
            return 2*a+2*c
        else:
        return 2*min(a,b)+1+2*c
    a,b,c=map(int,input().split())
    print(f(a,b,c))