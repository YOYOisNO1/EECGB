    n=0
    m=0
    
def ByDay(day) :
    	if day <= m :
    		return n-day
    	return n - m + m*(day-m) - day*(day+1)/2 + m*(m+1)/2
    
def binary() :
    	first = 1
    	last = 1000000000000000000
    
    	while first + 1 < last :
    		mid = (first+last)/2
    
    		if ByDay(mid) <= 0 :
    			last = mid
    		else :
    			first = mid
    	if ByDay(first) <= 0 :
    		return first
    	else
    		return last					
    
    n,m = map(int,input().strip().split())
    
    
    print binary()	