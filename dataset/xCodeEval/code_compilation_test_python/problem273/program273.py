    import sys, os
    from math import sqrt, gcd, ceil, log, floor
    from bisect import bisect, bisect_left
    from collections import defaultdict, Counter, deque
    from heapq import heapify, heappush, heappop
    input = sys.stdin.readline
    read = lambda: list(map(int, input().strip().split()))
    # read_f = lambda file:  list(map(int, file.readline().strip().split()))
    
    # from time import time
    
    sys.setrecursionlimit(5*10**6)
    
    MOD = 10**9 + 7
    
    
def main():
    	# file1 = open("C:\\Users\\shank\\Desktop\\Comp_Code\\input.txt", "r")
    	# n = int(file1.readline().strip()); 
    	# arr = list(map(int, file1.read().strip().split(" ")))
    	# file1.close()
    	m, s =read()
    	# arr = []
    	t = s
    	if int(1*m) <= s <= int(9*m):
    		arr = [1]*m; s -= m
    		for i in range(m-1, -1, -1):
    			arr[i] += min(8, s)
    			s -= min(8, s)
    			if s == 0:break
    			# print(arr, s)
    		mini = 0
    		for i in arr:mini = mini*10 + i; #print(i, mini)
    
    		arr = [0]*m; s = t;
    		for i in range(m):
    			arr[i] += min(9, s)
    			s -= min(9, s)
    			if s == 0:break
    		maxi = 0
    		for i in arr:maxi = maxi*10 + i
    		print(mini, maxi)
    
    	else:
    		print("-1 -1")
    	
    
    
    
    
    
    
    	# file = open("output.txt", "w")
    	# file.write(ans+"\n")
    	# file.close()
    
    if __name__ == "__main__":
    	main()
    
    """
    
    
    
    
    
    
    
    
    
    """