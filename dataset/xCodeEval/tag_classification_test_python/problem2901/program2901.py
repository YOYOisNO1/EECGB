def program2901():
    import sys
    
    n = int(input())
    arr = list(input().split())
    temp = int(arr[0]) - int(arr[1])
    
    for i in range (1 , n-1) :
        if int (arr[i]) - int(arr[i+1]) != temp :
            print(arr[n-1])
            sys.exit()
    
    print((int(arr[n-1])) - temp)
    
    
    
    
    
    
    
    
    
    
    
    
    