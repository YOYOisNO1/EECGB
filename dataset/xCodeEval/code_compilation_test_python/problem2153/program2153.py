def program2153():
    # -*- coding: utf-8 -*-
    """
    Created on Thu Sep 21 20:36:12 2017
    
    @author: MetaMemeLord-
    """
    
    n = input()
    i = len(n)-1
    while i>0:
        if n[i] == '0':
            del n[i]
    for i in range(len(n)//2):
        if(n[i]!=n[n-i-1])
            print('NO')
        else:
            print('YES')
            