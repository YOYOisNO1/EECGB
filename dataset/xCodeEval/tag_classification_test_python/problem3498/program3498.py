def program3498():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    a[0],a[n-1] = a[n-1],a[0]
    print(' '.join([str(i) for i in a]))