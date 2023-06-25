def program48():
    import math
    
    cups = 0.0
    medals = 0.0
    shelves = 0.0
    
    for c in range(0,2):
        cups = cups + float(input( ))
        
    for c in range(0,2):
        medals = medals + float(input( ))
        
    shelves = float(input())
    
    cups = math.ceil( cups / 5 )
    medals = math.ceil( medals / 10 )
    total = cups + medals
    if shelves >= total:
        print("YES")
    else:
        print("NO")
       