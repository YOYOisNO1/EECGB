def program5458():
    n = int(input())
    (x, y) = [int(i) for i in input().split()]
    
    dist1 = (min(x,y) + abs(x-y) -1)
    dist2 = (min(n-x,n-y) + abs(x-y))
    
    if dist1 <= dist2:
        print("White")
    else:
        print("Black")