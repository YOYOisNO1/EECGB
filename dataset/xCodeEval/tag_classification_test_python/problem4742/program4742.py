def program4742():
    n, m = map(int, input().split())
    if n > m:
        l, r = 1, 2 * 10 ** 18 + 1
        while r - l > 1:
            k = (l + r) // 2
            if k * (k + 1) // 2 < n - m:
                l = k
            else:
                r = k
        if l * (l + 1) // 2 < n - m:
            k = r
        else:
            k = l
        print(m + k)
    else:
        print(n)