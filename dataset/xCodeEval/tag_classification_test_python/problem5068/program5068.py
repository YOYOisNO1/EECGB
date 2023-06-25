    #from itertools import product, permutations, combinations, accumulate, compress
    #from collections import Counter, defaultdict, deque # deque([iterable[, maxlen]]) #appendleft popleft rotate
    #from heapq import heapify, heappop, heappush # func(heapifiedlist, item)
    #from bisect import bisect_left, bisect_right, insort # func(sortedlist, item)
    # TODO: more coping mechanisms...?
    #from sys import setrecursionlimit
    
    import os, sys
    input = lambda: sys.stdin.buffer.readline().rstrip(b'\r\n')
    
def dbp(*args, **kwargs): # calling with dbp(locals()) is perfectly cromulent
    	print(*args, file=sys.stderr, **kwargs)
    
    a_str = lambda: input().decode('ascii')
    get_int_list = lambda: [int(x) for x in input().split()]
    join_str = lambda l, ch=' ': ch.join((str(x) for x in l))  # ch is a default, not kwarg
    
def do_thing():
    	x, y = get_int_list()
    
    	q = [x]
    	seen = set()
    	while q:
    		x = q.pop()
    		#dbp(bin(x))
    		if x == y:
    			return 'YES'
    		seen.add(x)
    		xbstr = bin(x)[2:]
    		ystr1, ystr2 = (xbstr+'0')[::-1], (xbstr+'1')[::-1]
    		y1 = int(ystr1, 2)
    		if y1 < y*4 and y1 not in seen:
    			q.append(y1)
    		y2 = int(ystr2, 2)
    		if y2 < y*4 and  y2 not in seen:
    			q.append(y2)
    	
    	return 'NO'
    
    if __name__ == "__main__":
    	maxcc = 1
    	#maxcc = int(input())
    	for cc in range(maxcc):
    		print(do_thing())