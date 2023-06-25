    from math import floor
    
def gt(t,g,r):
    	zt=floor(t)
    	rt=t-zt
    	zt%=(g+r)
    	t=zt+rt
    	if t<g:
    		return 0
    	else:
    		return r+g-t
    
    l,d,v,g,r=[int(x) for x in input().split(' ')]
    t=d/v
    t+=gt(t,g,r)
    t+=(l-d)/v
    print(t)