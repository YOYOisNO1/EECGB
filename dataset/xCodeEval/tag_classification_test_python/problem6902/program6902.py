def program6902():
    for i in range(input()):
        a, b, m = map(int, input().split())
        if a == b:
            print(1,) a
            continue
        n, k = 2, 1
        while 1:
            l, r = k * (a + 1), k * (a + m)
            if l <= b <= r:
                d = b - l
                print(n,) a,
                ans = [1] * (n - 1)
                k >>= 1
                last = 0
                for i in range(n - 2):
                    if d >= k:
                        x = min(d / k, m - 1)
                        d -= x * k
                    else:
                        x = 0
                    if i == 0:
                        ans[i] = a + 1 + x
                    else:
                        ans[i] = ans[i - 1] * 2 - last + 1 + x
                    last = 1 + x
                    k >>= 1
                ans[-1] = b
                print(' ').join(map(str, ans))
                break
            if l > b:
                print(-1)
                break
            n += 1
            k <<= 1