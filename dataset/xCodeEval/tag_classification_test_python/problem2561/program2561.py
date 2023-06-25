def program2561():
    from math import gcd
    n = int(input())
    l = list(map(int,input().split()))
    gcd1 = 0
    for i in l:
    	gcd1 = gcd(i,gcd1)
    print(n*gcd1)	