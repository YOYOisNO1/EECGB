    import math
    import operator
def is_acute(p,q,r):
      pq = list(map(operator.sub, p, q))
      rq = list(map(operator.sub, r, q))
      dot_prod = sum(i[0]*i[1] for i in zip(pq, rq))
      norm_pq = math.sqrt(sum(i[0]*i[1] for i in zip(pq,pq)))
      norm_rq = math.sqrt(sum(i[0]*i[1] for i in zip(rq,rq)))
      cos_pqr = dot_prod / (norm_rq * norm_pq)
      arccos_pqr = math.acos(cos_pqr)
      if math.degrees(arccos_pqr) < 90:
        return True
      else:
        return False
    
    n = int(input())
    points = []
    for i in range(n):
      points.append(list(map(int, input().split())))
    
    bad_points = set()
    for i in range(n):
      for j in range(n):
        for k in range(n):
          if i == j or j == k or k == i:
            continue
          if i in bad_points:
            continue
          if is_acute(points[j], points[i], points[k]):
            bad_points.add(i)
            continue
    
    print(n - len(bad_points))
    for i in range(n):
      if i not in bad_points:
        print(i+1, end=' ')