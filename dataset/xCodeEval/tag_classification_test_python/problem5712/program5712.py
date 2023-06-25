    from fractions import gcd
    import sys
    x, y, n = [int(x) for x in input().split()]
    
def f(x, y):
        g = gcd(x, y)
        return x/g, y/g
    
    x, y = f(x, y)
    if y <= n:
        print("{}/{}").format(x,y)
    else:
        m = 1
        ans_a, ans_b = 1, 1
        for b in xrange(1,n+1):
            i = x*b/y
            for a in [i,i+1]:
                if abs(a*y-x*b) < m*b*y:
                    m = abs(float(a)/b-float(x)/y)
                    ans_a, ans_b = a, b
        ans_a, ans_b = f(ans_a, ans_b)
        if y*(2*ans_a-1) == 2*ans_b*x and ans_a - 1 >= 1:
            ans_a -= 1
        ans_a, ans_b = f(ans_a, ans_b)
        print("{}/{}").format(ans_a,ans_b)