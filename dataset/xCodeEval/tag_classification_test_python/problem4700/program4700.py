def program4700():
    n, k = map(int, input().split())
    S = map(lambda c: ord(c) - ord('A'), input())
    
    F = [n]*26
    L = [0]*26
    
    for i in range(n):
      L[S[i]] = i
    for i in range(n-1, -1, -1):
      F[S[i]] = i
    
    res = 0
    cur = 0
    for i in range(n):
      if F[S[i]] == i: cur += 1
      res = max(res, cur)
      if L[S[i]] == i: cur -= 1
    
    if res > k: print('YES')
    else: print('NO')