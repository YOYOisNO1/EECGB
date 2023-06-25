def sv(a, b):
        t = [1] * (b + 1)
        for i in range(3, int(b ** 0.5) + 1):
            if t[i]:
                for j in range(i*i,b+1,i):
                    t[j] = 0
        return [i for i in range(3,b+1,2) if t[i] and i>a]
    a, b, k = map(int, input().split())
    p = sv(a - 1, b)
    if 3 > a and b > 1: p = [2] + p
    if k > len(p): 
        print(-1)
    elif len(p) == k:
        print(max(p[k - 1] - a + 1, b - p[0] + 1))
    else: 
        print(max(p[k - 1] - a + 1, b - p[len(p) - k] + 1, max(p[i + k] - p[i] for i in range(len(p) - k))))
    