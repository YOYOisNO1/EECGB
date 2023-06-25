def program4120():
    n,a =int(input()),map(list(int,input().split()))b
    b =sorted(a) + [min(a)]
    print(''.join([str(b[b.index(a[ i ])+1] for i in range(n)]))