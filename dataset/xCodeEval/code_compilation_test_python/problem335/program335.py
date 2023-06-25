    from itertools import combinations
    
def is_triangle(tri):
    	a,b,c = tri
    	if a+b <= c:
    		return False
    	if a+c <= b:
    		return False
    	if c+b <= a:
    		return False
    	return True
    
    n = int(input())
    a = list(map(int, input().split()))
    
    c = list(combinations(a, 3))
    
    truth = False
    for tri in c:
    	if is_triangle(tri):
    		truth = True
    		break
    
    print(["NO","YES"][truth])