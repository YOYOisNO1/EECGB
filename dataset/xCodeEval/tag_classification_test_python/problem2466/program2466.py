    import itertools
    from fractions import gcd
    from math import sqrt
    from bisect import bisect_right
    #headache
def get(a):
    	return map(a , input().split())
def I():
    	return int(input())
def Str():
    	return input()
    
    n = input()
    har = input()
    ansi = ""
    ansj = ""
    resi , resj = 0, 0
    fg = False 
    for i in har:
    	if i == '(':
    		fg = True
    	if i == ')':
    		fg = False
    	if fg:
    		if (i != '(' and i != ')'):ansj += i
    		if (i == '(' or i == ')'):ansj += '_'
    	else:
    		if (i != '(' and i != ')'):ansi += i
    		if (i == '(' or i == ')'):ansi += '_'
    
    try:
    	ab = ansj.split('_')
    	resj = 0
    	for i in ab:
    		if len(i):
    			resj += 1
    except:resj = 0
    try:
    	ab = ansi.split('_')
    	resi = 0
    	for i in ab:
    		resi = max(resi , len(i))
    except:resi = 0
    
    #print(ansj)
    #print(ansi)
    print(resi) , resj
    	