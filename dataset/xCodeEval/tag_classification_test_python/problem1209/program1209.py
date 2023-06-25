    from sys import stdin
    input = stdin.buffer.readline
    
def func():
    	if a == b == c == d == 0:
    		print(0)
    	elif a == b == c == d == 1:
    		print(2)
    	else:
    		print(1)
    
    
    for _ in range(int(input())):
    	a, b = list(map(int, input().split()))
    	c, d = list(map(int, input().split()))
    	func()