def program416():
    hh,mm = input().strip().split(":")
    mm = int(mm) + 1
    hh = int(hh)
    if mm > 59:
    	mm -= 60
    	hh += 1
    if hh > 23:
    	hh -= 24
    mm = '%02d' % mm
    hh = '%02d' % hh
    while hh != mm[::-1]:
    	mm = int(mm) + 1
    	hh = int(hh)
    	if mm > 59:
    		mm -= 60
    		hh += 1
    	if hh > 23:
    		hh -= 24
    	mm = '%02d' % mm
    	hh = '%02d' % hh
    print(hh+":"+mm)