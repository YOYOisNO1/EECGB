def program888():
    a = int(input())
    n = a
    
    found = 0
    for i in range(2):
        j = 2
        while j * j <= a:
            if a % j == 0:
                found += 1
                a /= j
                break
            j += 1
    
    if found == 0:
        print "1"
        print "0"
    elif found == 1:
        print "2"
    else:
        print "1"
        print n / a
    