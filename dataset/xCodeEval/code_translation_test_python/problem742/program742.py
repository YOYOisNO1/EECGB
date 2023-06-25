    '''input
    7 13 18
    2 6 12
    '''
    import math
def solve():
    	l1,r1,t1 = list(map(int,input().split()))
    	l2,r2,t2 = list(map(int,input().split()))
    	# diff  = l1-l2+k1*t1-k2*t2
    	# diff  = l1-l2 + K*gcd(t1,t2)
    	# l2-l1 / gcd(t1,t2) = K
    	g = math.gcd(t1,t2)
    	K1 = (l2-l1)//g 
    	K2 = (l2-l1)//g 
    	if((l2-l1)%g!=0):
    		K2+=1
    	diff1 = l1-l2 + K1*g
    	diff2 = l1-l2 + K2*g
    	if t1==t2:
    		print(min(r1,r2)-max(l1,l2)+1)
    		return
    	#print(diff1,diff2)
    	ans = 0
    	for i in [diff1,diff2]:
    		l22 = l2+i
    		r22 = l22+r1-l1
    		ans = max(ans,min(r22,r2)-max(l22,l2)+1)
    	print(ans)
    	return
    t = 1
    #t = int(input())
    while t>0:
    	t-=1
    	solve()