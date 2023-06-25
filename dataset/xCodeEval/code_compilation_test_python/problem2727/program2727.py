def program2727():
    n=int(input())
    a=[]
    b=[]
    count=0
    for i in range(n):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(n):
        if a[i] in b:
            count+=b.count(a[i))
    print(count)        