def program4229():
    from sys import exit
    
    x = input()
    for a in xrange(1, x + 1):
        for b in xrange(1, a + 1):
            if a % b == 0:
                if a * b > x:
                    if a / b < x:
                        print(a,) b
                        exit()
    
    print(-1)