    from math import gcd
    
def lcm(a, b):
        return (a*b)//gcd(a, b)
    
    n = int(input())
    a = list(map(int, input().split()))
    
    ok = True
    cp = []
    
    for i in range(n):
        v = [0]*n
        v[i] = 1
        p = a[i]-1
        c = 1
        
        while p != i:
            if v[p] == 1:
                ok = False
                break
            v[p] = 1
            p = a[p]-1
            c += 1
        
        cp.append(c//2 if not c%2 else c)
        
    if ok:
        l = 1
    
        for i in cp:
            l = lcm(l, i)
    
        print(l)
    else:
        print(-1)
            
            
    #components:
        # if any component does not lead back to initial value, print(-1)
        # if len(component) = 2, treat it as 1
        # otherwise, len(component) stays same
        # find lcm of len(i) for i in components
            