def program130():
    from math import sqrt
    n = int(input())
    k = int((sqrt(8*n+1)-1)/2)
    a = range(1,k+1)
    for i in xrange(1,n-k*(k+1)/2+1):
    	a[-1*i]+=1
    print(k)
    for i in xrange(k):
    	print(a[i],)