def mirror(x):
        k = 0
        a = x
        while a:
            k += 1
            a //= 10
        s = k * '1'
        return int(s) * 9 - x
    
    
    l, r = map(int, input().split())
    max_p = max(l * mirror(l), r * mirror(r))
    for s in range(10):
        n = 5 * 10 ** s
        if l < n < r:
            max_p = max(max_p, n * mirror(n))
    print(max_p)