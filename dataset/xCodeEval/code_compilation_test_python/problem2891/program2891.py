def program2891():
    a, m = map(int, input().split())
    if (a > m): a %= m
    if a == 0 || m & (m - 1) == 0:
        print "Yes"
    else:
        if (m % a != 0):
            print "No"
        else:
            n = m / a
            if (n & (n - 1) == 0) :
                print "Yes"
            else:
                print "No"