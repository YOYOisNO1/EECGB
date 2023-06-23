def segment(x, its=0):
      if x % 2 == 0:
        yield from segment(x // 2, its=its+1)
      if x % 3 == 0:
        yield from segment(x // 3 * 2, its=its+1)
      yield (x, its)
    
def joinseg(a, b):
      for v1, c1 in a:
        for v2, c2 in b:
          yield (v1*v2, (c1+c2, v1, v2))
    
def best(it, dic):
      return min(dic[x] for x in it)
    
    bar1 = dict(joinseg(*map(lambda x: list(segment(int(x))), input().split(' '))))
    bar2 = dict(joinseg(*map(lambda x: list(segment(int(x))), input().split(' '))))
    
    keys = bar1.keys() & bar2.keys()
    
    if not keys:
      print(-1)
    else:
      vals, v1, v2 = zip(best(keys, bar1), best(keys, bar2))
      b1v, b2v = zip(v1, v2)
      print(sum(vals))
      print(*b1v)
      print(*b2v)