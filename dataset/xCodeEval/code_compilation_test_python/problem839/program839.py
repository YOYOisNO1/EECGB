def fun(a,b):
        if b==1:
            return a
        else:
            return ((a//b)+1)+fun(a%b,(b-(a%b)))
    a,b=map(int,input().split())
    print fun(a,b)