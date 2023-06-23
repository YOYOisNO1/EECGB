def program2187():
    # -*- coding: utf-8 -*-
    """
    Created on Mon May 25 14:38:46 2020
    
    @author: Ritvik Agarwal
    """
    n, wps = input(), map(int, input().split())
    i, summ = 0, 0
    while summ < n:
        if i == 7:
            i = 1
        else:
            i += 1
        summ += wps[i-1]
    print i