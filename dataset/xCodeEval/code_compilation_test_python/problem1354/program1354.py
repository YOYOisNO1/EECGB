def program1354():
    n = int(input())
    a = [int(_) for _ in input().split()]
    sum = 0
    for x in a:
        sum += x          
        
    if sum % 2 != 0:                                          
        print(0)
        exit(0)                                             
    for i in range(n):                                       
        if a[i] % 2 != 0:
            print(1)                                                print(i + 1)
            exit(0)
                                                      
    mn = 2000 + 10
    for x in a:                                         
        mn = min(mn, x)
    
    print(1)
    print(mn)