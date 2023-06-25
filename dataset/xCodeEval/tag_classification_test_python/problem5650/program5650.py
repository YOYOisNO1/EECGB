def program5650():
    c = input()
    c = c.split()
    c = list(map(int, c))
    a, b = c
    if(a > b):
        n = b
    else: 
        n = a
    f = 1        
    while(n != 1):
        f = f * (n)
        n = n - 1
    
    print(f)
    
    
       