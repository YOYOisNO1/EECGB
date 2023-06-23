def program2002():
    # Problem statement: http://codeforces.com/problemset/problem/14/C
    
    I = map(int, input().split())
    #print I
    
    d = {} # dictionary
    x, y = 0, 0 
    for i in xrange(4):
        x1, y1, x2, y2 = I[4*i], I[4*i+1], I[4*i+2], I[4*i+3]
        # print (x1, y1) , (x2 , y2)
        x += (x1 == x2 and y1 != y2)
        y += (y1 == y2 and x1 != x2)
        d[(x1,y1)] = d.get((x1,y1),0) + 1 # The get function of dictionary
        d[(x2,y2)] = d.get((x2,y2),0) + 1
    
    if any(z != 2 for z in d.values()): print 'N0' ; exit() #the any() function
    print 'YES' if (x == 2 and y == 2) else 'NO'
    
    # lambda w: int(w)
    # I[4*i], I[4*i+1], I[4*i+2], I[4*i+3]