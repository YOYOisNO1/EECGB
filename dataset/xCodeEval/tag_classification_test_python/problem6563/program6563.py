def program6563():
    import sys
    import fractions
    import string
    
    n,k= map(int, input().split())
    a = [int(i) for i in input().split()]
    d = n / k
    ret = 0
    for i in range(k):
        c = [0] * 3
        for j in range(d):
            c[ a[i+j*k] ] += 1
        ret += min(c[1], c[2])
    print(ret)