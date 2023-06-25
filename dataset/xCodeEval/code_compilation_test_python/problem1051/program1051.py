def program1051():
    # # # coding=utf-8
    # # # Author: lee215
    
    get = lambda: int(input().strip())
    getl = lambda: input().strip()
    gets = lambda: map(int, input().strip().split())
    getss = lambda n: [gets() for _ in xrange(n)]
    
    
    T = get()
    for _ in xrange(T):
        s = getl()
        if "".join(sorted(s)) in "abcdefghijklmnopqrstuvwxyz":
            print "Yes"
        else:
            print "No"