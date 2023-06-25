def program76():
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    for i in range(a):
        count=b.count(b[i])
        if count>c:
            c=count
    print(c)