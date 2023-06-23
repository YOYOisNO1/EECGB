def program2995():
    px, py, vx, vy = map(int, input().split())
    
    pd = px + py
    vd = max(vx, vy)
    
    if pd <= vd:
        print 'Polycarp'
        quit()
    else:
        pc, pc1, vc, vc2 = [px, py], [px, py], [vx, vy], [vx, vy]
        f1, f2 = False, False
        #print pc, vc
        for _ in xrange(vd):
    
    	if pc[0] != 0:
    	    pc[0] -= 1
    	else:
    	    pc[1] -= 1
    
    	if pc1[1] != 0:
    	    pc1[1] -= 1
    	else:
    	    pc1[0] -= 1
    
    	if 0 not in vc:
    	    vc[0] -= 1
    	    vc[1] -= 1
    	elif vc[1] == 0:
    	    vc[0] -= 1
    	else:
    	    vc[1] -= 1
    
    	if vc2[0] > vc2[1]:
    	    vc2[0] -= 1
    	elif vc2[1] > vc2[0]:
    	    vc2[1] -= 1
    	else:
    	    vc2[0] -= 1
    	    vc2[1] -= 1
    
    	#print pc, vc, vc2
    	if vc in [pc, pc1]:
    	    #print 'Polycarp'
    	    f1 = True
    	if vc2 in [pc, pc1]:
    	    f2 = True
    
        if f1 and f2:
    	print 'Polycarp'
        else:
    	print 'Vasiliy'