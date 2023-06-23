    
    # stdin = open("testcase.txt")
    
# def input():
    # 	return stdin.readline().strip()
    
    
    # import io, os
    # import sys
    
     # sys.stdout.write(str( (n-1)*(n-2) + 1 ) + "\n")
    # input = io.BytesIO(os.read(0, \
    #          os.fstat(0).st_size)).readline
    # from math import log
    # # import sys
    import sys
    sys.setrecursionlimit(1000000000)
    from collections import Counter, defaultdict
    from queue import PriorityQueue
    from bisect import bisect_left
    mod = 1000000007
def integer_list():
    	return list(map(int, input().split()))
    
def string_list():
    	return list(map(str, input().split()))
    
def hetro_list():
    	return list(input().split())
    
    	
    
    
    
    
    
    t = int(input())
    
    
    for _ in range(t):
    	x = int(input())
    	lst = integer_list()
    	next_ = lst[x-1]
    
    	if next_ == 0:
    		print("NO")
    	else:
    		next_ = lst[next_ - 1]
    		if next_ == 0:
    			print("NO")
    		else:
    			print("YES")
    
    
    
    
    
    
    
    
    
    			
    
    
    
    
    
    
    
    
    	
    
    
    
    
    
    
    
    
    
    
    	
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    		
    
    
    
    
    			
    
    
    	
    
    
    	
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    