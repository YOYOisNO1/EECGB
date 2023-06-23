    #!/usr/bin/python
    import sys
    
def f(x, s, index, length):
    	a = int(s[index])
    	if index == length - 1:
    		return 2 if (a + x) % 2 == 1 else 1
    	if (a + x) % 2 == 0:
    		return f( (a+x)/2, s, index+1, length)
    	else:
    		return f( (a+x)//2, s, index+1, length) + \
    			   f( (a+x)//2+1, s, index+1, length)
    
def selfInclude(s):
    	for i in range(0, len(s)-1):
    		a = int(s[i])
    		b = int(s[i+1])
    		if abs(a-b) > 1:
    			return False
    	return True
    
    s = sys.stdin.readline().strip()
    result = 0
    for i in range(10):
    	result += f(i, s, 1, len(s))
    print result-1 if selfInclude(s) else result