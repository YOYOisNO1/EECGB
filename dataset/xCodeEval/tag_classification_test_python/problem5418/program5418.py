    M = 1000000007
    
def solve(n, k):
      if k == 0: return 1
    
      p = pow(2, n - 1, M)
      q = pow(2, n, M)
    
      if n % 2 == 0:
        p -= 1
        d0 = 0
        d1 = 0
        for i in range(k):
          if i == 0:
            d0 = p
            d1 = 1
          else:
            d1 = (d1 * q + d0) % M
            d0 = (d0 * p) % M
        return (d0 + d1) % M
      else:
        return pow(p + 1, k, M)
    
    
    t = int(input())
    for i in range(t):
      n, k = map(int, input().split())
      print(solve(n, k))