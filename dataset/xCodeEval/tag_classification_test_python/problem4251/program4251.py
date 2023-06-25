    from sys import *
    from collections import *
    from math import *
    
    input = stdin.readline
    
    global a, b, c, d
    
def binary_search(y, sum):
    	lo = a
    	hi = b
    	id = -1
    	while lo <= hi:
    		mid = (lo + hi) // 2
    		cnt = min(mid + y, d + 1) - c
    		cnt = max(cnt, 0)
    		if cnt >= sum:
    			hi = mid - 1
    			id = mid
    		else:
    			lo = mid + 1
    	return id
    
    if __name__ == "__main__":
    	a, b, c, d = map(int, input().split())
    	triangle = 0
    	for y in range(b, c + 1):
    		start = binary_search(y, 1)
    		if start is -1:
    			continue
    		cnt1 = min(start + y, d + 1) - c
    		cnt1 = max(cnt1, 0)
    		cnt2 = min(b + y, d + 1) - c
    		cnt2 = max(cnt2, 0)
    		end = binary_search(y, cnt2)
    		if end is -1:
    			continue
    		len1 = end - start
    		sum = (2 * cnt1 + (len1 - 1)) * len1 // 2
    		len2 = b - end + 1
    		sum += len2 * cnt2
    #		print(y, start, end, cnt1, cnt2, sum)
    		triangle += sum
    	print(triangle)