def program1254():
    n, k = map(int, input().split())
    fib, i = [1, 1], 1
    for j in range(2, 50):
      fib.append(fib[j - 1] + fib[j - 2])
    while (i <= n):
      if (k <= fib[n - i]):
        print(i,)
        i = i + 1
      else:
        print(i) + 1, i,
        k, i = k - fib[n - i], i + 2