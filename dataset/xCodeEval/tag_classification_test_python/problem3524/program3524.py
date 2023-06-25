def program3524():
    n = int(input())
    m = 0
    ls = list(map(int,input().split()))
    for i in range(n+1):
        s = 0
        for j in range(i) : s+=(not ls[j])
        for j in range(i,n) : s+=ls[j]
        m = max(s,m)
    print(m)