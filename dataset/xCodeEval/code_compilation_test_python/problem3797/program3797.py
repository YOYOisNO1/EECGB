def program3797():
    
    n, m, a, b = map(int, input().split())
    
    start = a % m
    end = b % m
    if start == 0: start = m
    if end == 0: end = m
    
    
    start_l = (a - 1) / m
    end_l = (b - 1) / m
    
    
    if start_l == end_l:
      print 1
    elif start_l + 1 == end_l:
      if start == 1 and (b == n or end == m):
      else:
        print 2
    else:
      ans = 1
      if start != 1:
        ans += 1
      if end != m and b != n:
        ans += 1
    
      if start == end + 1:
        ans = min(ans, 2)
    
      print ans