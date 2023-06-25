    '''input
    1
    '''
     
     
     
    from bisect import bisect_right as bl
    from random import randint as R
    RI = lambda : [int(_x) for _x in input().split()]
    
    
    
    
    
    n = input()
    
    c = [1]*10
    
def pro(l):
    	p=1
    	for i in l:
    		p*=i
    	return p
    
    cur = 0
    while pro(c)<n:
    	c[cur]+=1
    	cur = (cur+1)%10
    ans = ""
    e=0
    for i in "codeforces":
    	ans+=c[e]*i
    	e+=1
    print(ans)