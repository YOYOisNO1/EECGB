def program2605():
    sw = input()
    s1 = input()
    s2 = input()
    sw = sw.split(' ')
    s1 = s1.split(' ')
    s2 = s2.split(' ')
    
    curW = sw[0]
    curH = sw[1]
    st1W = s1[0]
    st1H = s1[1]
    st2W = s2[0]
    st2H = s2[1]
    while(curH > 0 ):
    	curW += curH
    	if curH == st1H:
    		curW -= st1W
    	elif curH == st2H:
    		curW -+ st2W
    	curH -= 1
    return curW
    	