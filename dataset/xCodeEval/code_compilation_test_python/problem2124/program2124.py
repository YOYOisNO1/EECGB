def program2124():
    inpu_t = int(input())
    
    for i in range(inpu_t, inpu_t + 10 ):
        if int(i[-1,-3]) % 4 == 0:
            return i
            break
    
            