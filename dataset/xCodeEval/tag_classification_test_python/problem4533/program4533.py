def program4533():
    #!/usr/bin/env python
    
    Vp = int(input().strip())
    Vd = int(input().strip())
    T = int(input().strip())
    f = int(input().strip())
    c = int(input().strip())
    res = 0
    x = Vp*T 
    y = 0
    if Vp >= Vd:
    	res = 0
    else:
    	while (True):
    		t = 1.0*x / (Vd-Vp)
    		if x + t*Vp<c:
    			res += 1
    			x += (f+2*t)*Vp
    		else:
    			break
    
    print(res)
    
    