def program2363():
    #!/usr/bin/env python2
    
    occ = []
    for i in range(300):
        occ.append(0)
    pair = {}
    k = 0
    i = 0
    while i < 300:
        while i < 300 and occ[i] == 1:
            i += 1
        if i == 300:
            break
        occ[i] = 1
        if i+k < 300:
            occ[i+k] = 1
        pair[i] = i+k
        k += 1
    #print pair
    
    n = int(input())
    
    if n == 1:
        a = int(input())
        if a == 0:
            print "BitAryo"
        else:
            print "BitLGM"
    
    elif n == 2:
        a, b = map(int, input().split())
        if pair[a] == b or pair[b] == a:
            print "BitAryo"
        else:
            print "BitLGM"
    
    else:
        a, b, c = map(int, input().split())
        if (a^b^c) == 0:
            print "BitAryo"
        else:
            print "BitLGM"