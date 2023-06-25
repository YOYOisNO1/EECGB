    MODULO = int(1e9) + 7
    
def findnumways(n ,d_state, k, d, num_ways):
    	if n < 0:
    		return 0
    	if n == 0 and not d_state:
    		return 0
    	if n == 0 and d_state:
    		return 1
    	
    	if (n,d_state) in num_ways:
    		return num_ways[(n,d_state)]
    
    	cnt = 0
    	for i in range(1, k+1):
    		if i < d: 
    			cnt += (findnumways(n-i, False or d_state, k, d, num_ways)%MODULO)
    		else:
    			cnt += (findnumways(n-i, True, k, d, num_ways)%MODULO)
    	num_ways[(n,d_state)] = cnt % MODULO
    	return cnt % MODULO
    
    
    if __name__ == '__main__':
    	n, k, d = map(int, input().split())
    	num_ways = dict()
    	
    	print(findnumways(n, False, k, d, num_ways) % MODULO)