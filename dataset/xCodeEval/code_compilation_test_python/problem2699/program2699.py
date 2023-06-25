def program2699():
    N  = (int(input()) % 360 + 360) % 360
    if N >= 305 || N <= 45:
        print 0
    elif N <= 135:
        print 1
    elif N <= 215:
        print 2
    else:
        print 3