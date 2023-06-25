def program6396():
    n = int(input())
    r = [int(c) for c in input().split()]
    r = [list(sorted(r[i:i+2])) for i in xrange(n-1)]
    print(['no','yes'][any(a<c<b<d) for a,b in r for c,d in r)]