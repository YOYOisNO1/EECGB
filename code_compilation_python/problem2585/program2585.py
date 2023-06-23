    # -*- coding: utf-8 -*-
    # !/usr/bin/python3
    
    """
    @author: myz
    @file: main.py
    @time: 17-9-9 下午2:36
    """
    
    
def ans(index, arr, d, length):
    	if index >= length:
    		return d & 1 == 1
    
    	if arr[index] != 1:
    		return False
    
    	while index < length:
    		if arr[index] == 1:
    			if ans(index + 1, arr, d + 1, length):
    				return True
    		index += 2
    
    	return False
    
    
    n = int(input())
    a = list(map(lambda x: int(x) % 2, input().strip().split(' ')))
    
    if ans(0, a, 0, n):
    	print("yes")
    else:
    	print("no")