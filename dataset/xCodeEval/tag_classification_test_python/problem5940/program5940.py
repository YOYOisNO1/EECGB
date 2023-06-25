    '''input
    4
    2 1 4 3
    '''
def gcd(a, b):
      """Return greatest common divisor using Euclid's Algorithm."""
      while b:      
          a, b = b, a % b
      return a
    
def lcm(a, b):
      """Return lowest common multiple."""
      return a * b // gcd(a, b)
    
def lcmm(*args):
      """Return lcm of args."""   
      return reduce(lcm, args)
    
    n = int(input())
    c = map(int, input().split())
    
    l = []
    v = [False] * n
    
    fail = False
    p = 0
    while (p < n):
      if v[p]:
        p += 1
        continue
      v[p] = True
      m = set()
      m.add(p)
      pp = c[p] - 1
      ll = 1
      while pp not in m:
        if v[pp]:
          fail = True
          break
        else:
          v[pp] = True
          m.add(pp)
          pp = c[pp] - 1
          ll += 1
        # print(m)
      if fail or pp != p:
        fail = True
        break
      elif pp == p:
        if ll % 2 == 1:
          l.append(ll)
        else:
          l.append(ll / 2)
        p += 1
    
    if fail:
      print(-1)
    else:
      print(lcmm(*l))