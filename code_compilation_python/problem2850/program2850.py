def program2850():
    # -*- coding: utf-8 -*-
    """
    Spyder Editor
    
    This is a temporary script file.
    """
    
    
    
    #s1 = "10 30".split()
    #s1 = "10 35".split()
    #s1 = "05:20".split(":")
    
    s1 =input().split()
    a = int(s1[0])
    ta = int(s1[1])
    
    s1 =input().split()
    b = int(s1[0])
    tb = int(s1[0])
    
    s1 =input().split()
    h = int(s1[0])
    m = int(s1[1])
    departT = ((h-5)*60+m)/a*a
    
    count = 0
    for b0 in range(0, 18*6, b):
        b1 = b0+tb
        if departT < b1 and departT+ta < b0:
            count +=1 
            
    print count