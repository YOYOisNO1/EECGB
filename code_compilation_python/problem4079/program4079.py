def program4079():
    v1 = int(input())
    v2 = int(input())
    t = int(input())
    d = int(input())
    
    ans = 0
    for i in range(0,t):
    	ans=ans+min(v1+d*i,v2+d*(t-i-1))
    print ans
    
    #v1, v2 = map(int, input().split())
    #t, d = map(int, input().split())
    #print sum(min(v1 + d * i, v2 + d*(t-i-1)) for i in xrange(t))