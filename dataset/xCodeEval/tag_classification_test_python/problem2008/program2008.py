    #!/usr/bin/env pypy
    from __future__ import division, print_function
    from collections import defaultdict, Counter, deque
    from future_builtins import ascii, filter, hex, map, oct, zip
    from random import randint
    from itertools import imap as map, izip as zip, permutations, combinations, combinations_with_replacement
    from __builtin__ import xrange as range
    from math import ceil, log
    from _continuation import continulet
    from cStringIO import StringIO
    from io import IOBase
    import __pypy__
    from bisect import bisect, insort, bisect_left, bisect_right
    import sys
    import os
    import re
    inf = float('inf')
    mod = int(1e9) + 7
    mod_ = 998244353
    N = int(1e5) + 5
    
    '''
    Check for special cases (n=1)
    One wrong submission = 10 mins penalty!
    do smth instead of nothing and stay organized
    '''
    
def main():
    	n, k, d = map(int, input().split())
    	# dp[n][is] = # of paths with total wt = n (is = 0 : all edges wt < d, is = 1 : atleast 1 edge wt >= d)
    	dp = [[0]*2 for i in range(101)]
    	dp[0][0] = 1
    	dp[0][1] = 0
    
    	for i in range(1, n+1):
    		# i is the target wt
    		for j in range(1, k+1):
    			# j is the edge wt ur taking (<= k)
    			# u cant take edge wt > target wt
    			if j > i:
    				break
    
    			if j < d:
    				# for is = 0 we cant take edge with wt >= d
    				dp[i][0] = (dp[i][0] + dp[i-j][0]) % mod
    
    				# for is = 1 if ur taking edge with wt < d
    				# u shudve picked an edge with wt >= d before
    				dp[i][1] = (dp[i][1] + dp[i-j][1]) % mod
    			else:
    				# if ur taking edge of wt >= d, u couldve taken edges 
    				# with wt < d or >= d before so we can add dp with is = 1/0
    				dp[i][1] = (dp[i][1] + dp[i-j][0]) % mod
    				dp[i][1] = (dp[i][1] + dp[i-j][1]) % mod
    
    	# our target wt is n and is=1 
    	print(dp[n][1])
    
    
    
    BUFSIZE = 8192
    class FastI(IOBase):
	def __init__(self, file):
    		self._fd = file.fileno()
    		self._buffer = StringIO()
    		self.newlines = 0
     
	def read(self):
    		while True:
    			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
    			if not b:
    				break
    			ptr = self.buffer.tell()
    			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
    		self.newlines = 0
    		return self.buffer.read()
     
	def readline(self):
    		while self.newlines == 0:
    			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
    			self.newlines = b.count("\n") + (not b)
    			ptr = self._buffer.tell()
    			self._buffer.seek(0, 2), self._buffer.write(
    				b), self._buffer.seek(ptr)
    		self.newlines -= 1
    		return self._buffer.readline()
    class FastO(IOBase):
	def __init__(self, file):
    		self._fd = file.fileno()
    		self._buffer = __pypy__.builders.StringBuilder()
    		self.write = lambda s: self._buffer.append(s)
     
	def flush(self):
    		os.write(self._fd, self._buffer.build())
    		self._buffer = __pypy__.builders.StringBuilder()
def print(*args, **kwargs):
    	sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    	at_start = True
    	for x in args:
    		if not at_start:
    			file.write(sep)
    		file.write(str(x))
    		at_start = False
    	file.write(kwargs.pop("end", "\n"))
    	if kwargs.pop("flush", False):
    		file.flush()
def gcd(x, y):
    	while y:
    		x, y = y, x % y
    	return x
    sys.stdin, sys.stdout = FastI(sys.stdin), FastO(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")
    if __name__ == "__main__":
	def bootstrap(cont):
    		call, arg = cont.switch()
    		while True:
    			call, arg = cont.switch(to=continulet(
    				lambda _, f, args: f(*args), call, arg))
    	cont = continulet(bootstrap)
    	cont.switch()
    	main()