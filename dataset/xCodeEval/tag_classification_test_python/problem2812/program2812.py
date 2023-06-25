def program2812():
    n, k = input().strip().split()
    k = int(k)
    n = list(n)
    cnt_zero = n.count('0')
    if cnt_zero < k:
        print(len(n) - 1)
    else:
        res, cnt = 0, 0
        n.reverse()
        for c in n:
            if c == '0': cnt += 1
            else: res += 1
            if cnt == k: break
        print(res)