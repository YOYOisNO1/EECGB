def program2803():
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    n, m, k = [int(i) for i in input().strip().split()]
    prices = [int(i) for i in input().strip().split()]
    nearest = 10 * n
    for i in range(n):
    	if(prices[i] != 0 and prices[i] <= k):
    	    if(nearest >  abs(i + 1 -  m) * 10):
    			nearest =  abs(i + 1 - m) * 10
    print(nearest)		