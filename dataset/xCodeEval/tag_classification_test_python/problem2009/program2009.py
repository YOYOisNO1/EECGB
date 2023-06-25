    dpall = []
    dpd = []
    MOD = 1000000007
    n, k, d = map(int, input("").split(" "))
    for i in range(105):
      dpall.append(None)
      dpd.append(None)
    
def solveD(u):
      if u == 0:
        return 1
      if dpd[u] != None:
        return dpd[u]
      ans = 0
      for i in range(1, min(min(d - 1, k), u) + 1):
        ans += solveD(u - i)
      dpd[u] = ans
      return ans
    
def solveAll(u):
      if u == 0:
        return 1
      if dpall[u] != None:
        return dpall[u]
      ans = 0
      for i in range(1, min(k, u) + 1):
        ans = ans + solveAll(u - i)
      dpall[u] = ans
      return ans
    
    res = solveAll(n) - solveD(n)
    print(res % MOD)