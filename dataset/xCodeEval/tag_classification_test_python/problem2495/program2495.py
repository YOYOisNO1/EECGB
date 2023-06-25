def program2495():
    n = input()
    m = input()
    L = []
    K = []
    for i in m :
        L.append(int(i))
    
    for i in n :
        K.append(int(i))
    #print(L)
    #print(K)
    buf = ''
    for i in xrange(len(L)):
        buf += str(L[i] ^ K[i])
    print(buf)