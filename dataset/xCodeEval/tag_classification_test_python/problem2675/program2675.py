def solve():
    	d1, d2, d3 = [int(x) for x in input().split()]
    	print(min(d1+d2+d3,d1+d3+d1+d3,d2+d3+d2+d3,d2+d2+d1+d1))
    
    # t = int(input())
    # for x in xrange(t):
    # 	solve()
    solve()