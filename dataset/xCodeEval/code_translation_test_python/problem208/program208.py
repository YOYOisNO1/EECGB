def program208():
    from fractions import gcd
    t,w,b = [int(r) for r in input().split()]
    
    ans = min(w,b)
    lcm = w*b/gcd(w,b)
    ans = ans*(t/lcm +1)
    ans -= 1
    last_num = t/lcm * lcm
    ans -= max(0,last_num+min(w,b)-1-t)
    den = t
    print(str(ans/gcd(ans,den))+"/"+str(den/gcd(ans,den)))
    
    1,2,12,13,14,24,25