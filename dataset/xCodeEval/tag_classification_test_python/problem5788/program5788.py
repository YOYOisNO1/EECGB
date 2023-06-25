def program5788():
    n = int(input())
    a = list(map(int,input().split()))
    MIN,cnt = 1e9,0
    for i in range(n) :
        MIN = min(MIN,a[i])
    for i in range(n) :
        if a[i] == MIN :
            cnt += 1
    if 2*cnt > n :
        print("Bob")
    else :
        print("Alice")