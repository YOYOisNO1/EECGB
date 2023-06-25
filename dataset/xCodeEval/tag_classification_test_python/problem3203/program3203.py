def program3203():
    n = input()
    s = sorted(map(int,input().split()))
    r = 0
    for i in xrange(n/2):
        r +=s[2*i+1]-s[2*i]
    print(r)