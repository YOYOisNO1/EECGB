def program1742():
    import math
    R = lambda: map(int, input().split())
    l,r,a,b = R()
    if b % a:
        print(0)
        quit()
    i = 1
    res = 0
    #print(i,int(math.sqrt(b)))
    b //= a
    while i <= int(math.sqrt(b)):
        #print(i*i,int(math.sqrt(a*b)))
        if b % i == 0 and math.gcd(b//i,i) == 1:
            if l <= (b//i)*a <= r and l <= i*a <= r:
                res += 1
                #print(b//i,i)
                if b//i != i:
                    res += 1
        i += 1
    print(res)