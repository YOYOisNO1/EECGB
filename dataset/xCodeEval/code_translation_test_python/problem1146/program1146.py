def program1146():
    n, maxh, rest = list(map(int, input().strip().split()))
    a = [maxh]*n
    
    for i in range(rest):
        l, r, m = list(map(int, input().strip().split()))
        for i in range(l - 1, r):
            a[i] = min(a[i], m)
    
    print(sum(i*i for i in a))