def program675():
    n, r = map(int, input().split()
    
    arr = map(int, input().split()
    
    oper = 0
    
    arr.sort()
    mini = 0
    
    while mini < arr.length(): 
        
        if mini == r:
            
            oper += 1
            mini += 1
            continue
        
        if mini == arr[mini]:
            
            mini += 1
            continue
        
        else:
            
            oper += 1
            mini += 1
            
    print oper
        
        
        