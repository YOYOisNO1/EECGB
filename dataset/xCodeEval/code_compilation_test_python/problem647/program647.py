def program647():
    n,m = map(int, input().split()))
    s = list(map(int, input().split())))
    s.sort()
    minim = max(s) - min(s)
    for i in range(m-n+1):
    	if ( s[i+n-1]-s[i] < minim):
    		minim = s[i+m-n]-s[i]
    		
    print minim		