def program804():
    n=int(input())
    a=list(map(int,input().split()))
    p=a
    x=max(a)
    while(x <= 1000):
        s = (n*x)-sum(a)
        if s > sum(a):
            print(x)
            break
        else:
            x+=1