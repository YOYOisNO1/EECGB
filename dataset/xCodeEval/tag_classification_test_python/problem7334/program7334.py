def program7334():
    from collections import *
    
    cost = []
    for _ in [0,1,2]: 
      cost.append(map(int, input().split()))
    N = int(input())
    d = defaultdict(int)
    
    for n in xrange(1,N+1):
      for i in xrange(3):
        for j in xrange(3):
          if i==j: continue
          other = min(x for x in [0,1,2] if x!=i and x!=j)
          way1 = d[n-1,i,other] + d[n-1,other,j] + cost[i][j]
          way2 = 2*d[n-1,i,j] + d[n-1,j,i] + cost[i][other] + cost[other][j]
          d[n,i,j] = min(way1,way2)
    
    print(d[N,0,2])