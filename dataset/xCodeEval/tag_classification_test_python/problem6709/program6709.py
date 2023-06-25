    from collections import deque
    n = input()
    cost = {}
    
def ones(x):
    	ans = 0
    	for i in range(x):
    		ans *= 10
    		ans += 1
    	return ans
    
def numdigits(x):
    	tmp = x
    	ans = 0
    	while (tmp != 0):
    		ans += 1
    		tmp /= 10
    	return ans
    
    cost[n] = 0
    length = numdigits(n)
    
    for cur_digits in range(length, 0, -1):
    	#remove nodes corresponding to numbers with more than cur_digits
    	cost = {key:val for key,val in cost.items() if key <= ones(cur_digits+1)}
    
    	#now relax edges
    	q = deque()
    	d = ones(cur_digits)
    	dd = ones(cur_digits+1)
    
    	for key, val in cost.items():
    		q.append((key,val))
    
    	while len(q) != 0:
    		cur_num, cur_cost = q.popleft()
    
    
    		tmp_num = cur_num - d
    		if tmp_num >= 0:
    			if (tmp_num not in cost) or (cost[tmp_num] > cur_cost + cur_digits):
    				cost[tmp_num] = cur_cost + cur_digits
    				q.append((tmp_num, cost[tmp_num]))
    				#print(tmp_num, cost[tmp_num])
    
    		tmp_num = dd - cur_num
    		if (tmp_num not in cost) or (cost[tmp_num] > cur_cost + cur_digits):
    			cost[tmp_num] = cur_cost + cur_digits +1
    			q.append((tmp_num, cost[tmp_num]))
    			#print(tmp_num, cost[tmp_num])
    
    print(cost[0])
    
    