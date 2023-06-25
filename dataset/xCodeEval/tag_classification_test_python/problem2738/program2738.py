def program2738():
    n = int(input())
    a = list(map(int,input().split()))
    b = set(a)
    l = len(b)
    if l==2:
        b=list(b)
        if (b[1]-b[0])%2==0:
            print(abs((b[1]-b[0])//2))
        else:
            print(abs((b[1]-b[0])))
    elif l==3:
        b = list(b)
        b.sort()
        if b[1]-b[0]==b[2]-b[1]:
            print(b[1]-b[0])
        else:
            print(-1)
    elif l==1:
        print(0)
    else:
        print(-1)