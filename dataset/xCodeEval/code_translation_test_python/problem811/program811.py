def program811():
    x1,y1,x2,y2 = [int(_) for _ in input().split()]
    x,y = [int(_) for _ in input().split()]
    
    diff = x2-x1,y2-y1
    
    if x != 0:
        diff = diff[0] % (2*x),diff[1]
    
    if y != 0:
        
        diff = diff[0], diff[1] % (2*y)
    
    if diff in [(x,y),(x,-y),(-x,y),(-x,-y),(0,0)]:
        print("YES")
    else:
        print("NO")