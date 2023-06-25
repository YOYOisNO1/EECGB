def solve():
    	# Input
    	gl = list(input())
    	rl = list(input())
    	cl = list(input())
    	
    	
    	# Calculations
    	r = True
    	while cl:
    		if cl[0] in gl:
    			gl.pop(gl.index(cl[0]))
    			cl.pop(0)
    		elif cl[0] in rl:
    			rl.pop(rl.index(cl[0]))
    			cl.pop(0)
    		else:
    			r = False
    			break
    			
    	if gl or rl:
    		r = False
    	
    	# Output
    	if r:
    		print('YES')
    	else:
    		print('NO')
    	
    	
    
    
    if __name__ == '__main__':
    	solve()