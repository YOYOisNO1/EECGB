    import sys
    
def f(a):
    	if a == '>':
    		return 1
    	elif a == 'v':
    		return 2
    	elif a == '<':
    		return 3
    	else:
    		return 4
def g(a):
    	if a == '>':
    		return 1
    	elif a == '^':
    		return 2
    	elif a == '<':
    		return 3
    	else:
    		return 4
    
    
    
    inital, final = input().split()
    n = input()
    s = f(inital) + n
    t = g(inital) + n
    if t > 4:
    	if t % 4 != 0:
    		t = t % 4
    	else:
    		t = 4		
    if s > 4:
    	if s % 4 != 0:
    		s = s % 4
    	else:
    		s = 4
    if s == f(final) and t == g(final):
    	print('undefined')
    	sys.exit()
    
    
    if t == g(final):
    	print('ccw')
    	sys.exit()
    
    print('cw')