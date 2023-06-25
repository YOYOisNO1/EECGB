def program6262():
    n = input()
    mod = 10**9 + 7
    if n == 0:
      print(1)
    else:
      print(((pow(2,) n-1, mod) * (1 + pow(2, n, mod))) % mod)