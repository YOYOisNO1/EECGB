    import sys
    from math import sqrt, gcd, ceil, log, floor
    # from bisect import bisect, bisect_left
    from collections import defaultdict, Counter, deque
    from heapq import heapify, heappush, heappop
    input = sys.stdin.readline
    read = lambda: list(map(int, input().strip().split()))
    
    # sys.setrecursionlimit(200000)
    
def main():
    	# ans_ = []
    	lis = []
	def f(x):
    		if x > n:return
    		lis.append(x)
    		f(x*10)
    		f(x*10+1)
    	n = int(input())
    	f(1)
    	print(len(lis))
    	# 	ans_.append(str(ans))
    	# print(("\n").join(ans_))
    if __name__ == "__main__":
    	main()