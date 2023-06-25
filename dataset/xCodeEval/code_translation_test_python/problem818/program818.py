def program818():
    import Queue
    from collections import Counter
    import math
    import bisect
    #sys.stdin = open('input.txt', 'r')
    #sys.stdout = open('output.txt','w')
    
    N = int(input())
    A = []
    for k in xrange(1,N+1) :
        if k*(k+1)/2 > N :
            break
        A += k*(k+1)/2,
    dic = {key : True for key in A}
    for x in A :
        if N-x in dic :
            print('YES')
            exit(0)
    print('NO')