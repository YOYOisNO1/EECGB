def program957():
    import math
    T,S,q = map(int,input().split())
    rate = (q-1)/float(q)
    count = 1
    timer = 0
    step = 0.1
    
    while round(S,3) < T:    
        if timer > S:
            count += 1        
            timer = timer - S + step*0.5
        
        step = math.ceil((S-timer)*100)/100000
        #if timer - S < 1:
        #    if timer - S < 0.1:
        #        step = 0.01
        #    else: step = 0.1
        #else: step = 1
        
        timer += step
        S += rate*step
    print count