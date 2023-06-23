def program1506():
    s = "<>+-.,[]"
    
    t = '';
    for c in input():
        t += bin(8+s.index(c))[2:]
    print t
    #n = 0;
    for i in xrange(len(t)):
        n = (n + int(t[len(t) - 1 - i]) * pow(2,i)) % 1000003
    #    print n
    print int(t, 2) % 1000003
    #print n