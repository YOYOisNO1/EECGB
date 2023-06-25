    n, k = map(int, input().split())
def V(x):
      return (2 * k - x - 1) * x / 2 + 1
    a, b=0, k
    while a < b:
      m = (a + b) / 2
      if n > V(m):
        a = m + 1
      else:
        b = m
    print(a) if a < k else -1
    