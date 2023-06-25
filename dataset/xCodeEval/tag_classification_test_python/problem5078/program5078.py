def program5078():
    if __name__ == '__main__':
    	#n,a,b,c,d = 2,1,1,1,2
    	n,a,b,c,d = map(int,input().split())
    	p = 0
    	for i in xrange(1,n+1):
    		t = a+b+i
    		t1,t2,t3 = t-a-c,t-b-d,t-c-d
    		if max(t1,t2,t3) <= n:
    			if min(t1,t2,t3) > 0:
    				p += 1
    		else:
    			break
    		#print(i,t1,t2,t3)
    	print(p*n)