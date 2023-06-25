def program3726():
    n,d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    count = 0
    a.sort()
    p = []
    for i in range(n):
        q = a[i] + d
        for j in range(n):
            if (a[j]<=q and a[j]>=a[i]):
                count+=1
        p.append(n-count)
        count = 0
    print((min(p)))