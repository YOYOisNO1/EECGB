def solve(num):
    	lst = list(num)
    
    	lst = [int(i) for i in lst]
    
    	target  = sum(lst)
    	if len(set(lst)) == 1:
    		return True
    	for i in range(target - 1, -1, -1):
    		if helper(lst, i, 0, 0):
    			return True
    	return False
    
    
def helper(lst, target, idx, subtotal):
    	if idx == len(lst):
    		if subtotal == 0:
    			return True
    
    		return False
    	if subtotal + lst[idx] == target:
    		return helper(lst, target, idx + 1, 0)
    
    	if subtotal + lst[idx] < target:
    		return helper(lst, target, idx + 1, subtotal + lst[idx])
    
    	return False
    
    
    
    n = input()
    x = input()
    if solve(x):
    	print(("YES"))
    else:
    	print(("NO"))