def program1330():
    from math import floor
    
    n, k, m, d = [int(i) for i in input().split()]
    #n, k, m, d = 23925738098196565, 23925738098196565, 23925738098196565, 1000
    #n, k, m, d = [int(i) for i in '1000000000000000000 100000000000000000 1 1000'.split()]
    
    ans = 0
    
    for i in range(1, d + 1):
        cur = int(n // (k * (i - 1) + 1))
        if m < cur:
    	    cur = m
        if cur * i > ans:
            ans = cur * i
    
    print(ans)