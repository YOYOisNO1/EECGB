    import sys,bisect as bi
    input = sys.stdin.readline
    I = lambda : list(map(int,input().split()))
    
def an(x,y):
    	vd=[1,x]+([] if x%2 else [2,x//2])
    	for i in range(3,int(x**0.5)+1,2):
    		if x%i==0:
    			vd.append(i)
    			if i!=x//i:
    				vd.append(x//i)
    	vd.sort()
    	an=4*x+4*y
    	for i in range(len(dv)):
    		cr=dv[i]
    		p=bi.bisect(vd,cr)
    		p-=1
    		if (x+y)//cr>=x//vd[p]:
    			an=min(an,2*(cr+(x+y)//cr))
    	return an
    a,b = I()
    x=a+b
    dv=[1,x]+([] if x%2 else [2,x//2])
    ar=[1,2,3]
    for i in range(3,int(x**0.5)+1,2):
    	if x%i==0:
    		dv.append(i)
    		if i!=x//i:
    			dv.append(x//i)
    print(min(an(a,b),an(b,a)))