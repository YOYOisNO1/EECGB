def program4288():
    """
    CONTESTENT: ngtien2
    CONTEST: Codeforces Round #306 (Div. 2)
    LANGUAGE: Python 2.7
    PROBLEM: B. Preparing Olympiad
    """
    
    n, l, r, x = map(int, input().split())
    c = map(int, input().split())
    
    count = 0
    for i in xrange(2**n):
        hard = 1
        easy = 10**6
        total = 0
        items = 0
        for j in xrange(n):
            if i&(1<<j) > 0:
                a = c[-j-1]
                if a > hard:
                    hard = a
                if a < easy:
                    easy = a
                total += a
                items += 1
        if items > 1 and x <= hard - easy and total >= l and total <= r:
            count += 1
    
    print(count)