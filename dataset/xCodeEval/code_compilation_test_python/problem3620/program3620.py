def next_permutation(a):
        k = len(a) - 2
        while a[k] > a[k+1]:
            k -= 1
        t = k + 1
        while t < len(a) - 1 and a[t+1] > a[k]:
            t += 1
        a[t], a[k] = a[k], a[t]
        sub = a[k+1:]
        sub.reverse()
        return a[:k+1] + sub
    
def count_current(a, x):
        r = 0
        for i in range(len(a) // 2):
            f = a[2*i]
            n = a[2*i + 1]
            r += x[f][n] + x[n][f]
        return r
    
def count(a, x):
        r, t = 0, a
        while len(t) > 1:
            r += count_current(t, x)
            t = t[1:]
        return r
    
    arr = []
    for i in range(5):
        arr.append([int(c) for c in input().split()])
    p = [0, 1, 2, 3, 4]
    res = 0
    while p != [4, 3, 2, 1, 0]:
        res = max(res, count(p, arr))
        p = next_permutation(p)
    print(res)