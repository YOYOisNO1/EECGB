    ## DATA SOURCE (1 for file, 0 for std input)
    opt = 0
    src = opt and open("input", "r") or None
    
def gvals(source, format = int, separator = ' '):
    	if source:
    		a = map(format, source.readline().split(separator))
    	else:
    		a = map(format, input().split(separator))
    	return a
    
def gval(source, format = int):
    	if source:
    		a = format(source.readline())
    	else:
    		a = format(input())
    	return a
    
    a, b, m, r0 = gvals(src)
    nums = [0]*m
    t = 1
    nums[r0] = 1
    while 1:
    	t += 1
    	r0 = (a*r0+b)%m
    	if nums[r0] == 0:
    		nums[r0] = t
    	else:
    		print(t-nums[r0])
    		break
    