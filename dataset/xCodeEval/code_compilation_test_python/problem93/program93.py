def gcd(a,b):
        if (b == 0):
            return a;
        else:
            return gcd(b, a%b);
    
    t,w,b = map(int, input().split())
    
    g = gcd(w, b);
    mn = min(w, b);
    ans = (w / g)*b;
    if (t%ans == 0):
        ans = ((t / ans) - 1)*mn + mn;
    else:
        ans = (t / ans)*mn + mn - 1;
    g = gcd(ans, t);
    ans /= g;
    t /= g;
    print(str(ans)+'/'+str(t))