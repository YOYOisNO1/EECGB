def solve(s):
        n, k, d = list(map(int, s.split()))
        return int((dp(n, k) - dp(n, d-1)) % 1000000007)
    
def dp(n, k):
        l = [2**i for i in range(k)]
        while len(l) < n:
            l.append(sum(l[-k:]))
        return l[n-1]
    
    s = input()
    print(solve(s))