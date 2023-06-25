def program3547():
    for i in range(n):
        a.append(input())
    
    s = 1000000000000
    for i in range(fact(k)):
        b = []
        
        for j in range(n):
            x = list(permutations(a[j]))[i]
            x = ''.join(x)
            x = int(x)
            b.append(x)
        
        mx = max(b)
        mn = min(b)
        
        if mx - mn < s:
            s = mx - mn
    
    print(s)