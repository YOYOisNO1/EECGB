def program4358():
    n = int(input())
    a = map(int,input().split(' '))
    t = int(input())
    m = 0
    for i in xrange(min(a),max(a)+1):
        tmp = 0
        for j in xrange(n):
            if a[j] in range(i,i+t+1):
                tmp += 1
        if tmp >m: m = tmp
    print m