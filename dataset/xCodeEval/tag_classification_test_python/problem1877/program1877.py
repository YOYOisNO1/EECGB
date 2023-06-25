def program1877():
    import sys
    
    n = int(input())
    if n <= 2:
        print(-1)
    else:
        a = [3,2]
        for i in xrange(2,n):
            a.append(1)
        print(' ').join(map(str,a))