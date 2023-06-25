def program3576():
    import sys
    
    #sys.stdin = open("input.txt")
    
    a, b, w, x, c = [long(x) for x in input().split()]
    
    
    t = c - a
    hash = {}
    
    if t <= 0:
        print 0
    else:
        cur_t = 0
    
        while 0 < t:
            #print cur_t
            if b >= x:
                if x <= 0:
                    print t
                    sys.exit()
                else:
    
                    cur_t += b/x
                    t -= b/x
                    b -= (b/x)*x
            else:
                if (w-x) <= 0:
                    print cur_t + (t-cur_t)/2
                    sys.exit()
                else:
                    delt = max((x-b)/(w-x),1)
                    b += (w-x)*delt
                    #t += delt
                    cur_t += delt
            if t >0:
                if b in hash:
                    del_t = t - hash[b][1]
                    del_step = cur_t - hash[b][0]
                    times = t / -del_t
                    cur_t += del_step*times
                    t += del_t * times
                else:
                    hash[b] = [cur_t, t]
    
        print cur_t + t