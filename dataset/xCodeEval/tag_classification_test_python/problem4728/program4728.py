    n = input()
    a = [int(x) for x in input().split()]
    
    # circle, triangle, square
    
def solve():
    	res = 0
    	for i in range(1, len(a)):
    		if (a[i-1], a[i]) in [(3,2), (2,3)]:
    			print('Infinite')
    			return
    
    		if (a[i-1],a[i]) in [(1,3), (3,1)]:
    			res += 4
    		else:
    			res += 3
    
    		if a[i] == 2 and i > 1 and a[i-1] == 1 and a[i-2] == 3:
    			res -= 1
    	print('Finite')
    	print(res)
    
    solve()
    
    