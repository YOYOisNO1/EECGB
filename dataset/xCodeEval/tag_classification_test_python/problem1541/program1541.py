    '''                      
       	
       			 ||Sri:||                 
    
                          __|
     ______________|_________________________
          |    |   ___|    |    |    ___|      |      |    |___
     /\  /\    |   |___    |    |   |___|      |      |    |___|
    /  \/  \   |   ___|    |    |         |_/    |___|    |___
    
    I am a beginner. Feel free to send tutorials/help to srinivasan1995@gmail.com.
    
    Codeforces, SPOJ handle: desikachariar.
    Hackerrank, Codechef handle: Prof_Calculus.
    
    Advices/Help are welcome. You will definitely get a thanks in return. Comments to be avoided.
    
    College: International Institute of Information Technology, Bangalore.
    
    '''
    
    import math
    
def fn():
    	return
    
    if __name__ == '__main__':
    	p, q = [pp for pp in input().split(' ')]
    	p = '0'+p
    	p = list(p)
    	#p = p.split()
    	q = int(q)
    	i = len(p)-1
    	posn = 0
    	while i >= 0 and q > 0:
    		posn = len(p)-1 - i
    		to_sub = ((int(p[i]) +1)%10) * (10 ** posn)
    		if to_sub > 0 and to_sub <= q:
    			p[i] = '9'
    			while(p[i-1] == '0'):
    				p[i-1] = '9'
    				i-=1
    			p[i-1] = str(int(p[i-1])-1)
    			q -= to_sub
    		i-=1
    	st = ""
    	i = 0
    	while p[i] == '0':
    		i+=1
    	while i < len(p):
    		st += p[i]
    		i+=1
    	print(st)	
    			