def program2074():
    # -*- coding: utf-8 -*-
    """
    Created on Thu Jun 11 07:56:57 2020
    
    @author: Harshal
    """
    
    
    n,k,d = [int(i) for i in input().split()]
    a = [[1],[1]]
    for i in range(1,n+1):
        a[0].append(sum(a[0][max(i-d+1,0):]))
        a[1].append(sum(a[1][max(i-k,0):]))
    print((a[1][-1]-a[0][-1])%(10**9+7))