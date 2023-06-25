def program3060():
    sides=map(int, input().split(" "))
    
    print((sides[1]+sides[0]+sides[2])*(sides[1]+sides[0]+sides[2])-sides[0]*sides[0]-sides[2]*sides[2]-sides[4]*sides[4])