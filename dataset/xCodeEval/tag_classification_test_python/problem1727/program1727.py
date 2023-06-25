def program1727():
    
    n , m = map(int,input().split())
    
    if n == 1 and m == 10:
        print(-1)
    else:
        print(m , end = '')
    
        if m == 10 :
            for i in range(1 , n-1):
                print('0',end = '')
    
        else:
            for i in range(1 , n):
                print('0' , end = '')
    
    
    
    