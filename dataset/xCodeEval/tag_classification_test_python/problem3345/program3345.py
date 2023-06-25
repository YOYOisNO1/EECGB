    import sys
    n = int(input())
    
    memo = [ -1 for i in xrange(100) ]
    memo[0] = 0
    memo[1] = 1
    
def fib(n):
      if n == 0:
        return 0
      if n == 1:
        return 1
      if memo[n] != -1:
        return memo[n]
    
      ret = fib(n-1)+fib(n-2)
      memo[n] = ret
      return ret
    
    
    i = 0
    while(True):
      f = fib(i)
      if n <= f:
        break
      i+=1
    for j in memo:
      for k in memo:
        for l in memo:
          if j != -1 and k != -1 and l != -1 and j + k + l == n:
            print(j,) k, l
            sys.exit(0)
    print("I'm too stupid to solve this problem")
    