def program3453():
    n, k = [int(x) for x input().split()]
    # list comprahension
    cnt = 0
    p = 2
    V = []
    
    while p<=n:
      if n%p==0:
        n = n // p
        cnt += 1
        V.append(p)
        if cnt==k:
          break
      else:
        p += 1
    
    if cnt==k and n>1:
      V[cnt-1] *= n
    
    if cnt<k:
      print(-1)
    else
      for i in range(0, k):
        print(V[i], end=' ')