    import math
    import operator
    PI = math.pi
    
def is_acute(p,q,r):
      pq = list(map(operator.sub, p, q))
      rq = list(map(operator.sub, r, q))
      dot_prod = sum(i[0]*i[1] for i in zip(pq, rq))
      norm_pq = math.sqrt(sum(i[0]*i[1] for i in zip(pq,pq)))
      norm_rq = math.sqrt(sum(i[0]*i[1] for i in zip(rq,rq)))
      cos_pqr = dot_prod / (norm_rq * norm_pq)
      arccos_pqr = math.acos(cos_pqr)
      if arccos_pqr < PI/2:
        return True
      else:
        return False
    
    n = int(input())
    points = []
    for i in range(n):
      points.append(list(map(int, input().split())))
    
    bad_points = [False for i in range(n)]
    for i in range(n):
      cond = False
      for j in range(n):
        for k in range(n):
          if i == j or j == k or k == i:
            continue
          if bad_points[i]:
            cond = True
            continue
          if is_acute(points[j], points[i], points[k]):
            bad_points[i] = True
            cond = True
            continue
          else:
            bad_points[j] = True
            bad_points[k] = True
        if cond:
          continue
      if cond:
        continue
    
    print(n - sum(bad_points))
    for i in range(n):
      if not bad_points[i]:
        print(i+1, end=' ')
    print('\n')