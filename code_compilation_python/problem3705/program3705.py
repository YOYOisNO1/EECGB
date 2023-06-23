    import math
    import operator
    
def angle(p,q,r):
      pq = list(map(operator.sub, p, q))
      rq = list(map(operator.sub, r, q))
      dot_prod = sum(i[0]*i[1] for i in zip(pq, rq))
      norm_pq = math.sqrt(sum(i[0]*i[1] for i in zip(pq,pq)))
      norm_rq = math.sqrt(sum(i[0]*i[1] for i in zip(rq,rq)))
      cos_pqr = dot_prod / (norm_rq * norm_pq)
      arccos_pqr = math.acos(cos_pqr)
      return math.degrees(arccos_pqr)
    
    n = int(input())
    points = []
    for i in range(n):
      points.append(list(map(int, input().split())))
    
    bad_points = [False for i in range(n)]
    for i in range(n):
      for j in range(n):
        for k in range(n):
          if i == j or j == k or k == i:
            continue
          if bad_points[i]:
            continue
          angle_jik = angle(points[j], points[i], points[k])
          if angle_jik < 90:
            bad_points[i] = True
            continue
          else:
            bad_points[j] = True
            bad_points[k] = True
    
    print(n - sum(bad_points))
    for i in range(n):
      if not bad_points[i]:
        print(i+1, end=' ')
    print('\n')