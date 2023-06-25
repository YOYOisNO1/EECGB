def program1648():
    
    t ={}
             
    
    t[0] = [int(x) for x in input().split(' ')]
    
    n , k = t[0][0], t[0][1]
    
    print(max(0, min(n + 1, k) - (k//2 + 1)) )