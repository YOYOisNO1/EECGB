    maxn = (int)(2e5 + 1)
    md = 998244353
    
    f = [1] * maxn
    for i in range(1, maxn):
      f[i] = (f[i-1] * i) % md
    inv = [1] * maxn
    for i in range(0, maxn):
      inv[i] = pow(f[i], md-2, md)
    
def binom(n, r):
      return (f[n] * inv[r] * inv[n-r]) % md
    
def solve(n, k):
      if k == 0: return f[n];
      if k >= n: return 0
    
      c = n - k
      sum = 0
      for i in range(0, c+1):
        if i & 1 == 0: sum += binom(c, i) * pow(c-i, n, md)
        else: sum -= binom(c, i) * pow(c-i, n, md)
    
      return (sum * binom(n, c) * 2) % md 
    
    n, k = map(int, input().split())
    
    print(solve(n, k))