def program1325():
    [N,V] = list(map(int,input().split()))
    
    
    reqpetrol = min(V,N-1)
    j = N-1-reqpetrol
    cost = reqpetrol
    i = 1
    
    while( j > 0 ):
         j -= 1
         cost += (i+=1)
         
    print(int(cost))
         