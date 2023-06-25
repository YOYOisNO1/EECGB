    n, p, t = map(float, input().split())
    n, t = int(n + 0.5), int(t + 0.5)
    from math import exp, lgamma
def c(a, b):     
      if a == b:
        return 1
      return exp(lgamma(a + 1) - lgamma(b + 1) - lgamma(a - b + 1))
    print(p)
    print(sum(p**i * (1 - p)**(t - i) * c(t, i) * min(i, n) for i in range(t + 1))) 