def check(a):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return True
        return False
    n = int(input())
    if n > 65:
        print(1)
    else:
        a = [int(i) for i in input().split()]
        xo = [0]
        for i in range(n):
            xo.append(xo[i] ^ a[i])
        ans = 1000
        for L1 in range(n):
            for R1 in range(L1 + 1, n):
                if check(a[:L1] + [xo[R1 + 1] ^ xo[L1]] + a[R1 + 1:]):
                    ans = min(ans, R1 - L1)
                    # print(L1, R1, ans)
                for L2 in range(R1 + 1, n):
                    for R2 in range(L2 + 1, n):
                        if check(a[:L1] + [xo[R1 + 1] ^ xo[L1]] + a[R1 + 1:L2] + [xo[R2 + 1] ^ xo[R1]] + a[R2 + 1:]):
                            ans = min(ans, R1 - L1 + R2 - L2)
                            # print(L1, R1, L2, R2, ans)
        print(ans if ans < 1000 else -1)
    