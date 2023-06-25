def program249():
    from itertools import permutations
    s=input()
    n=len(s)
    if(n&1):
        k=(n+1)//2
        print('4'*k+'7'*k)
    else:
        if(s>='99999999'):
            print('4444477777')
        else:
            k=n//2
            z='4'*k+'7'*k
            p='4'*(k+1)+'7'*(k+1)
            l=list(permutations(z))
            l=[''.join(x) for x in l]
            l.sort()
            for e in l:
                if(e>=s):
                    print(e)
                    exit(0)
            print(p)
            