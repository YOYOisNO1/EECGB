def program1443():
    import sys
    stickLength = int(sys.stdin.readline())
    
    
    """
    18 = {5,5,4,4} {1,1,8,8} {2,2,7,7} {3,3,6,6} 4 | -0
    16 = {5,5,3,3} {2,2,6,6} {7,7,1,1} 4 | -1
    14 = {5,5,2,2} {4,4,3,3} {6,6,1,1} 3 | -0
    12 = {5,5,1,1} {4,4,2,2} 3 | -1
    10 = {4,4,1,1} {2,2,3,3} 2 | -0 
    8 = {3,3,1,1} 2 | -1 
    6 = {2,2,1,1} 1 | -0
    4 = {1,1,2,2} 1 | -0
    2 = None
    
    if highest number is odd then its -1
    """
    n = 0
    elif stickLength == 4:
        n = 1
    elif stickLength >= 6:
        if ((stickLength/2) - 1) % 2 == 0:
            n = stickLength / 4
        else:
            n = (stickLength / 4) - 1
    
    print n