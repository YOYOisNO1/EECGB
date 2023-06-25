    a, b = map(int, input().split())
    
def rec(a, b):
    	if ((a // b) * b == a):
    		return a // b
    	if (a > b):
    		t = a // b
    		return t + rec(a - t * b, b)
    	else:
    		t = b // a
    		if (a * t == b):
    			t -= 1
    		return t + rec(a, b - t * a)
    
    print(rec(a, b))
    		