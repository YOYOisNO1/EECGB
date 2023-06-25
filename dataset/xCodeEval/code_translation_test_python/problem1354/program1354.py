def program1354():
    from __future__ import print_function
    import sys
    
    it = iter(sys.stdin.read().splitlines())
    n = int(next(it))
    
    lista = [0]*(n+1)
    for i in xrange(2, n+1):
        if(lista[i] == 0):
            for k in xrange(2*i, n+1, i):
                lista[k] = i
        lista[i] = i - lista[i] + 1
    pr = n
    for i in xrange(lista[n], n+1):
        pr = min(pr, lista[i])
    
    print(pr)