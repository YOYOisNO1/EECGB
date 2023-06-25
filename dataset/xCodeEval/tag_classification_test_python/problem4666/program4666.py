def program4666():
    # -*- coding: utf-8 -*-
    # from __future__ import division
    import sys
    
    n, k = [int(x) for x in sys.stdin.readline().split()]
    s = sys.stdin.readline().strip()
    
    A = ord('A')
    first = [None] * 26
    last = [None] * 26
    
    letter_nums = [(ord(c) - A) for c in s]
    
    for i in range(n):
    	if first[letter_nums[i]] is None:
    		first[letter_nums[i]] = i
    	last[letter_nums[i]] = i
    
    cur_n_segments = 0
    good = True
    
    for i in range(n):
    	if first[letter_nums[i]] == i:
    		cur_n_segments += 1
    		if cur_n_segments > k:
    			print('YES')
    			good = False
    			break
    	if last[letter_nums[i]] == i:
    		cur_n_segments -= 1
    if good:
    	print('NO')