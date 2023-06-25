def program61():
    import numpy
    k = int(input())
    l = [1]*10
    m = [c,o,d,e,f,o,r,c,e,s]
    p = numpy.prod(l) # product
    
    while p < k:
        for i in range(10):
            l[i] += 1 # increase number of alphabets
            p = numpy.prod(l)
            if p >= k:
                break
    
    s = ''
    for i in range(10):
        x = str(m[i])
        s += x*l[i]
    print(s)