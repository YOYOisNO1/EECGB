    from sys import *
    
    mod = 1000000007
    
def calc(n, k):
      if (k == 0):
        return 1
      if (k % 2 == 1):
        return (calc(n, k - 1) * n) % mod
      t = calc(n, k // 2)
      return (t * t) % mod
    
    n = int(stdin.readline())
    level = calc(2, n)
    print((level * (level + 1) // 2) % mod)
    