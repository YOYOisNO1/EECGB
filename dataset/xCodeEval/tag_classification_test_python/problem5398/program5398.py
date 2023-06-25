def program5398():
    ans = []
    q = 10 ** 9 + 7
    for _ in range(int(input())):
        n, k = map(int, input().split())
        if k == 0:
            ans.append(1)
            continue
        if n % 2 == 0:
            cur = 0
            p = 1
            pp = pow(2, n - 1, q) - 1
            pw = [1]
            cur_pw = 1
            mul = pow(2, n, q)
            for i in range(k - 2, -1, -1):
                cur_pw *= mul
                cur_pw %= q
                pw.append(cur_pw)
            pw.reverse()
            for i in range(k):
                cur += p * pw[i]
                cur %= q
                p *= pp
                p %= q
            cur += p
            cur %= q
        else:
            cur = 0
            p = 1
            pp = pow(2, n - 1, q) + 1
            for i in range(k):
                p *= pp
                p %= q
            cur += p
            cur %= q
        ans.append(cur)
    print('\n'.join(map(str, ans)))
        