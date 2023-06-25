    import sys
    readline = lambda: sys.stdin.readline().rstrip()
    write = sys.stdout.write
    
    import math
    
def calc(a, b, c):
    	sol = first_sol(a, b, c)
    	if not sol: return False
    	g, x, y = sol
    	left = math.ceil(-x*g*1.0/b)
    	right = math.floor(y*g*1.0/a)
    	return left <= right
    
def egcd(a, b):
    	if b==0: return (a, 1, 0)
    	g, x, y = egcd(b, a%b)
    	return (g, y, x-a/b*y)
    
def first_sol(a, b, c):
    	g, x, y = egcd(abs(a), abs(b))
    	if c%g: return None
    	x, y = x*c/g, y*c/g
    	if a < 0: x = -x
    	if b < 0: y = -y
    	return (g, x, y)
    
    
    a, b, c = [int(x) for x in readline().split()]
    if calc(a, b, c): write("Yes\n")
    else: write("No\n")