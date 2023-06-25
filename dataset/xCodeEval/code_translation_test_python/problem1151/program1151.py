    import itertools
    a, b, c, d = map(int, input().split())
def solve(a, b, c, d):
        ans = 0
        pre = [0]*(b + c + 2)
        for i in reversed(range(a, b + 1)):
            pre[i + b] += 1
            pre[i + c + 1] -= 1
        pre = list(itertools.accumulate(pre))
        pre = list(itertools.accumulate(pre))
        a = max(pre)
        last = 0
        for i in range(c, d + 1):
            if i < b + c + 1:
                last = a - pre[i]
            ans += last
        return ans
    
    print(solve(a, b, c, d))