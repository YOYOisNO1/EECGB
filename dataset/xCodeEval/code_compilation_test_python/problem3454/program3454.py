def program3454():
    n, k = [int(x) for x in input().split]
    p = 2
    V = []
    cnt = 0 #rozmiar listy czynników pierwszych
    
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
    else:
      for p in V:
        print(p, end=' ')