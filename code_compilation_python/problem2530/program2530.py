    import sys
    from collections import defaultdict
    from itertools import combinations
    from itertools import permutations
    input = lambda : sys.stdin.readline().rstrip()
def write(*args, sep="\n"):
      for i in args:
        sys.stdout.write("{}".format(i) + sep)
    INF = float('inf')
    MOD = int(1e9 + 7)
    
def prime(x):
      ret = []
      for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
          ret.append(i)
          ret.append(x // i)
      
      ret2 = []
      
      for i in ret:
        flag = True 
        for j in range(2, int(i**0.5) + 1):
          if i % j == 0:
            flag = False
            break 
        if flag:
          ret2.append(i)
      
      ret2.remove(1)
      return ret2
    
    x, n = map(int, input().split())
    ans = 1
    p = prime(x)
    #print(p)
    
    for i in p:
      s = 0
      for j in reversed(range(1, 65)):
        temp = i ** j
        if temp > n:
          continue
        else:
          # temp 로 나눠지는 것들의 개수 n // temp
          # print(n, temp, n // temp, s)
          ans *= pow(temp, n//temp - s, MOD)
          ans %= MOD 
          s += n // temp  - s
          ans %= MOD
          
    
    print(ans % MOD) 