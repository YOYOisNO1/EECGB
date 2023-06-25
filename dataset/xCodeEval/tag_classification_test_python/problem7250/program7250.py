def program7250():
    n, m, ans = map(int, input().split() + [0])
    f = [1] * 1005
    for i in range(1, 1005):
      f[i] = i * f[i -1]
    for i in range(1, 1 + min(n, m)):
      t = f[n] // (f[i] * f[n - i])
      for j in range(i):
        t *= (m - j) / (n * m - j)
      for j in range(n - i):
        v = n * m - i - j
        t *= (v - m + i) / (v)
      ans += (t * i * i) / n
    print(ans)