def program6571():
    import sys
    
    div = [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125]
    
    n,t = map(int,input().split())
    if t == 0:  print(0)
    elif n == 1:  print(1)
    else:
        d = {}
        for i in xrange(1,n+2):
            d[i] = [0 for j in xrange(i)]
    
        f = False
        for t1 in xrange(t):
            d[1][0] += 1
            for i in xrange(1,n+1):
                for j in xrange(i):
                    if d[i][j] > 1:
                        rem = d[i][j] - 1
                        d[i][j] = 1
                        d[i+1][j] += rem/2.0
                        d[i+1][j+1] += rem/2.0
                 
        c = 0
        for i in d:
            if i > n:   break
            for j in d[i]:
                if j == 1:  c += 1
        print(c)
                    
                        
                
                
                            
                    
                    
            
                
        
    
    
        