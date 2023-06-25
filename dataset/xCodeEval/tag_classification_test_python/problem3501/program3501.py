def program3501():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a[0],a[-1]=a[-1],a[0]
    print(' '.join([str(i) for i in a]))