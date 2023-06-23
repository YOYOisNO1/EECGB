def program772():
    # http://codeforces.com/problemset/problem/630/L
    
    import math
    
    n = str(input())
    
    n = n[0]+n[2]+n[4]+n[3]+n[1]
    
    n = int(n)
    n2 = 1
    
    for i in range(5):
      n2 = (n2*n) % 100000
    
    for i in range(5-len(n2))
      n2.insert(0,'0')
      
    print n2