def program546():
    n, m = map(int, input().split())
    f = [int(x) for x in input().split()]
    f.sort()
    x = []
    
    if n == m:
        print(max(f) - min(f))
    else:
        for i in range(m - n+1):
    
            x.append(abs(f[i] - f[i + n - 1]))
        print(min(x))