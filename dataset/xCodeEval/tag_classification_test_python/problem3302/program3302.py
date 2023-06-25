def program3302():
    from math import log, ceil
    n = int(input())
    if n == 1:
        print(1, 0)
        exit()
    
    f = {}
    i = 2
    while i <= n:
        if n%i == 0:
            f[i] = 0
            while n%i == 0:
                n = n//i
                f[i] += 1
        i += 1
    ans = 1
    for fi in f:
        ans = ans*fi
    pow2 = {1<<i for i in range(1, 21)}    
    
    fvalues = set(f.values())
    
    if fvalues == {1}:
        print(ans, 0)
    elif len(fvalues) == 1:
        v = fvalues.pop()
        if v in pow2:
            print(ans, ceil(log(v, 2)))
        else:
            print(ans, ceil(log(v, 2))+1)
    else:
        v = max(fvalues)
        print(ans, ceil(log(v, 2))+1)
        