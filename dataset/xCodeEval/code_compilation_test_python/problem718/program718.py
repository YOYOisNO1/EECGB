    # -*- coding: utf-8 -*-
    """
    Created on Mon Jul  1 16:11:00 2019
    
    @author: dake3
    """
    
    n, k = map(int, input().split())
    s = str(input())
    #n = length of string
    #k = size of set
    #s = string
    #n = 10
    #k = 100
    #s = 'ajihiushda'
    
    b = True
    
    if n>=k**2:
        print(k-1)
        b = False
    
    
def all_subs(word):
        sub = []
        for i in range(len(word)):
            for j in range(i, len(word)):
                sub.append(word[i:j+1])
        return set(sub)
    
    # Function which returns subset or r length from n 
    from itertools import combinations 
    
def rSubset(arr, r): 
    
    	# return list of all subsets of length r 
    	# to deal with duplicate subsets use 
    	# set(list(combinations(arr, r))) 
    	return list(combinations(arr, r)) 
    
    
    S = []
    S.append(s)
    
    for x in range(n):
        arr = list(s)
        S += [''.join(i) for i in rSubset(arr, x)]
    
    
    S = list(set(S))
    S.sort(key=len, reverse=True)
    
    if len(S) < k and b == True:
        print('-1')
    elif b == True:
        S = S[0:k]
        cost = 0
        for i in range(k):
            cost += n-len(S[i])
        print(cost)
    #print(S)
    #print(len(S))