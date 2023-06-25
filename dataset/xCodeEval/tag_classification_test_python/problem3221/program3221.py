    n, q = map(int, input().split())
    ops = []
    for i in range(q):
      ops.append(input().split())
    
def go(x, sz):
      if sz == n:
        return 1
      ret = 0
      for op in ops:
        if op[1] == x:
          ret += go(op[0][0], sz + 1)
      return ret
    print(go('a',) 1)