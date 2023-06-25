def program3733():
    import math
    
    input=[int(x) for x in input().split()]
    
    g=math.ceil(input[0]/input[2])
    
    singleOven=g*input[1]
        
    o1=0
    o2=input[3]
    
    for i in range(g):
        if o1<=o2:
            o1+=input[1]
        else:
            o2+=input[1]
    
    if max(o1, o2) < singleOven:
        print("YES")
    else:
        print("NO")
            