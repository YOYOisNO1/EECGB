    import sys
    import itertools
    import math
    
    
def solve(k, l):
      c = 1
      while l > k:
        l /= k
        c += 1
    
      if l == k:
        return c
      else:
        return None
        
    
    if __name__ == '__main__':
      k = int(input().rstrip())
      l = int(input().rstrip())
    
      if l % k == 0:
        tmp = solve(k, l)
        if tmp is not None:
          print("YES")
          print(tmp) - 1
        else:
          print("NO")
      else:
        print("NO")