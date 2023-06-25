def program2928():
    points = [(2,0),(1,-2),(-1,-2),(-2,0),(-1,2),(1,2)]
    
    ## find n such that , it lies on hexangon of length n+1
    
    l = int(input())
    
    lo = 1
    hi = 10**18
    
    while lo < hi :
        mid = lo + hi
        mid /= 2
        if 3 * mid *(mid+1) < l :
            lo = mid + 1
    
        else :
            hi = mid
    
    if 3 * lo *(lo+1) == l :
        print(2*lo,0)
    
    elif l!=0:
        ring = lo
        dist = 3 * ring *(ring +1 ) - l
        seg = dist / ring
        parity = dist % (ring)
        xslope = points[(seg+1)%6][0] - points[seg][0]
        yslope = points[(seg+1)%6][1] - points[seg][1]
        x = ring*points[seg][0] + xslope * parity
        y = ring*points[seg][1] + yslope * parity
        print(x,y)
    else :
        print(0) , 0