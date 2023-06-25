def program5966():
    C, Ha, Hb, Wa, Wb = map(int , input().split())
    
    ans = 0
    for i in xrange(1000000):
        if (C/Wa < i): break
        ans = max(ans, i * Ha + (C-i*Wa)/Wb * Hb)
        
    for i in xrange(1000000):
        if (C/Wb < i): break
        ans = max(ans, i * Hb + (C - i*Wb)/Wa * Ha)
        
    print(ans)