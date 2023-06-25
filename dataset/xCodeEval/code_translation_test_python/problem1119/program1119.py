def program1119():
    from sys import stdin
    n,m = map(int,stdin.readline().split())
    a = []
    f = m
    x = m
    m = -m
    while n:
     f = n/m
     if f * m > n:
      f +=1
     a.append(n - f * m)
     n = f
    
    print(len(a))
    for i in a:
     print((i) +x )%x,