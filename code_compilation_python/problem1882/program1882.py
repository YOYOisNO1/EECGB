def program1882():
    #! /usr/bin/env python
    
    import os
    import sys
    from math import *
    from scipy import stats
    import numpy as np
    from decimal import *
    from collections import Counter
    import timeit
    import time
    import matplotlib.pyplot as plt
    import re
    from itertools import permutations
    from itertools import combinations
    
    
    # if __name__ == '__main__':
    	
    	n, A = int(input()), list(map(int, input().split()))
    
    	
    	allZero = True
    	sum1 = 0
    	for i in range(n):
    		sum1 = sum1 + A[i]
    		if(A[i] != 0):
    			allZero = False
    
    	if(allZero == True):
    		print("NO")
    	elif(sum1 == 0):
    		for i in range(n):
    			if(A[i] != 0):
    				break
    		print("YES")
    		print("2")
    		print("1 " + str(i+1))
    		print(str(i+2) + " " + str(n))
    	else:
    		print("YES")
    		print("1")
    		print("1 " + str(n))