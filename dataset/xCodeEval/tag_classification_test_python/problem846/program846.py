def program846():
    
    
    n , m = map(int , input().split())
    
    x = [int(x) for x in input().split()]
    y = [int(y) for y in input().split()]
    
    for i in x:
        if i in y:
            print(str(i) , end = ' ')