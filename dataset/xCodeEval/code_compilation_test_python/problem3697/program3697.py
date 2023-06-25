def program3697():
    # coding: utf-8
    
    n, m = map(int, input().split())
    a = list()
    
    while n:
      a.append(n % m)
      n // m
      
    print('YES') if len(a) == len(set(a)) else print('NO')