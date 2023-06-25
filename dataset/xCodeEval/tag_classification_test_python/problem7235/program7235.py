def program7235():
    
    p1, p2, p3, p4, a, b = map(int, input().split())
    p_min = min(p1, p2, p3, p4)
    result = 0
    
    for x in range(a, b+1):
      if x == x % p_min:
        result += 1
    
    print(result)