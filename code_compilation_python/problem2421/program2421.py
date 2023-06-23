def program2421():
    t = input().split(":")
    t[0] = int(t[0])
    t[1] = int(t[1])
    
    min = t[1] * 6
    hr = (t[0] * 30 + t[1] * 0.5)%360
    
    print("{0} {1}".format(hr, min))