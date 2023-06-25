def program3558():
    n, t = map(int, input().split())
    
    s = list(input())
    s = map(lambda x : 0 if x == "G" else 1, s)
    
    l = -1
    
    for i in xrange(t) :
        j = 0
        while j < n-1 :
            if s[j] == 1 and s[j+1] == 0 :
                s[j] = 1 - s[j]
                s[j+1] = 1 - s[j+1]
                j += 1
            j += 1
    
    s = map(lambda x : "G" if x == 0 else "B", s)
    print('').join(s)
    