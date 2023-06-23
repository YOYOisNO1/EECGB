def program580():
    x,y = map(int,input().split())
    
    ma = x-y+1
    mi = (x//y)
    
    f= (ma*(ma-1))//2
    l = ((mi*(mi-1))//2)*y
    print(max((1,l),f)