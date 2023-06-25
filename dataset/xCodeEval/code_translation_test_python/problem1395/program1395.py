    #!/usr/bin/python
    
    from math import floor
    
    m = int(input())
    l = [k**3.0 for k in xrange(2,180000)]
    
def check(num):
        return m > check2(num)
    
def check2(num):
        return sum(floor(num/l[i]) for i in xrange(int(num**(1.0/3))))
    
    ma = 5 * 10**15
    mi = int(4.8 * m)
    
    while ma-mi > 1:
        mid = (ma+mi)/2
        if check(mid):
            mi = mid
        else:
            ma = mid
    
    if check2(ma) == m:
        print(ma)
    else:
        print(-1)