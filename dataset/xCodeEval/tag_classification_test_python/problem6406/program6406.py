def program6406():
    x=[int(w) for w in input().split()]
    t=[int(e) for e in input().split()]
    
    if max(t)>x[3]:
        print("Incorrect")
    elif min(t)<x[2]:
        print("Incorrect")
    elif (x[0]-x[1]==1) and (min(t)!=x[2] and max(t)!=x[3]):
        print("Incorrect")
    else:
        print("Correct")