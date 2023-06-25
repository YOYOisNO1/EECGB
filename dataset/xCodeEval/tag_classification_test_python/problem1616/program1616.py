def program1616():
    n,p = map(int,input().split())
    s = 0
    fa,fb,fc,fd,fe,ff = 0,0,0,0,0,1
    for a in range(10):
    	for b in range(10):
    		for c in range(10):
    			for d in range(10):
    				for e in range(10):
    					for f in range(10):
    						num = a*(10**fa)+b*(10**fb)+c*(10**fc)+d*(10**fd)+e*(10**fe)+f*(10**ff)+f*(10**max(0,ff-1))+e*(10**max(0,ff-2))+d*(10**max(0,ff-3))+c*(10**max(0,ff-4))+b*(10**max(0,ff-5))+a*(10**max(0,ff-6)) 
    						if len(str(num))%2==0 and num>0:
    							s = ((s)%p+(num)%p)%p
    							n-=1
    							if n==0:
    								print(s%p)
    								exit(0)
    					ff = max(2,ff)
    					fe = max(3,fe)
    				ff = max(3,ff)
    				fe = max(4,fe)
    				fd = max(5,fd)
    			ff = max(4,ff)
    			fe = max(5,fe)
    			fd = max(6,fd)
    			fc = max(7,fc)
    		ff = max(5,ff)
    		fe = max(6,fe)
    		fd = max(7,fd)
    		fc = max(8,fc)
    		fb = max(9,fb)
    	ff = max(6,ff)
    	fe = max(7,fe)
    	fd = max(8,fd)
    	fc = max(9,fc)
    	fb = max(10,fb)
    	fa = max(11,fa)