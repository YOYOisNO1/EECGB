def program3390():
    for _ in range(int(input())):
        n, k, d = map(int, input().split())
        a = list(map(int, input().split()))
     
        l = 105
        for i in range(n - d + 1):
            z = len(list(set(a[i:i + d])))
            l = min(l, z)
        print(l)