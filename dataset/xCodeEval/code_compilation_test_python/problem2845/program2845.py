def program2845():
    ﻿#python 3.6
    fib=[1,2]
    for i in range(90): 
    	fib.append(fib[-1]+fib[-2])
    
    n=int(input())
    for i in range(len(fib)):
    	if fib[i]>n:
    		print(i-1)
    		break
    
    