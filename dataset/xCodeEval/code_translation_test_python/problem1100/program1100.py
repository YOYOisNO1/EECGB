    #!/usr/bin/python
    import time
    import fractions
    
def lcm(a, b):
        """Return lowest common multiple."""
        return a * b // fractions.gcd(a, b)
    
    x,y,a,b = map(int, input().rstrip().split(" "))
    count = 0
    step = lcm(x,y)
    while a <= b:
        if a%x == 0 and a%y == 0:
            count += 1
            break
        a += 1
    if a < b:
        count += (b-a)/step
        #for i in xrange(a,b+1,step):
            #count += 1
    
    print(count)