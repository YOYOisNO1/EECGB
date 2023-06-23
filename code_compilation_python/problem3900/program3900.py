    n, k, a, b = map(int, input().split())
def sol(a, b):
    	c = a//b
    	print(c)
    
    if a < b:
    	a,b=b,a;
    sol(a,b)
    