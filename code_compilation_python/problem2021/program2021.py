def program2021():
      n, k = map(int, input().split())
      l = (2*n + 2*k + 2.25) ** (0.5) - 1.5
      print(int(n - l))