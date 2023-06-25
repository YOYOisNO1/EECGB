def gcd(m, n):
      if n:
        return gcd(n, m%n)
      else:
        return m
    
def lcm(m, n):
      return m*n//gcd(m,n)    
        
    n = int(input())
    arr = list(map(int, input().split()))
    seen = [False]*n
    res = 1
    
    for i, v in enumerate(arr):
      if res < 0:
        break
      cnt = 0
      k = i 
      while not seen[k]:
        seen[k] = True
        k = arr[k] - 1
        cnt += 1
      if k != i:
        res = -1
        break
      else:
        if not (cnt & 1):
          cnt //= 2
        if cnt:  
          res = lcm(res, cnt)  
    print(res)  
      