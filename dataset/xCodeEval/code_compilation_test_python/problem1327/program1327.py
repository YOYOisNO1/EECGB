def program1327():
    n, v = [int(x) for x in input().split()]
    if(n=v):
        x = v
        for i in range(2, n-v+1):
            x+=i
    else:
        x = n-1
    
    print(x)