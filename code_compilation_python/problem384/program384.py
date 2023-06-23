def program384():
    fat = min_1
    dead = min_2
    bad = min_3
    
    while fat+dead+bad<n:
        while fat<max_1:
            fat+=1
    
        while dead<max_2:
            dead+=1
    
        while bad<max_3:
            bad+=1
    
    print(fat dead bad)