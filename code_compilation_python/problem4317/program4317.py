def program4317():
    __author__ = 'neki'
    
    import sys
    
    #sys.stdin = open("friendsPresents.in", "r")
    #sys.stdout = open("friendsPresents.out", "w")
    
    words = input().split()
    cnt1 = int(words[0])
    cnt2 = int(words[1])
    x = int(words[2])
    y = int(words[3])
    #print(cnt1, cnt2, x, y)
    
    n = 1
    friend1 = 0
    friend2 = 0
    both = 1
    cond1 = 0
    cond2 = 0
    while cond1 == 0 or cond2 == 0:
        n += 1
        if n % x == 0:
            if n % y != 0:
                friend2 += 1
        else:
            if n % y == 0:
                friend1 += 1
            else:
                both += 1
        if friend1 + both >= cnt1 and friend2 + both >= cnt2:
            cond1 += 1
        if friend1 + friend2 + both >= cnt1 + cnt2:
            cond2 += 1
        #print(n, friend1, friend2, both)
    print(n)