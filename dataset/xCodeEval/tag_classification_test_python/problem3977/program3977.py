    (w, n) = (int(i) for i in input().split(" "))
    
    if w == 2:
        print("YES")
        exit(0)
    
    x = 1
    powers = []
    while x < 10e9:
        powers.append(x)
        x *= w
    
def myfind(n, powers):
    #    print("n=   "), n, powers
        if n == 0:
            return True
        if len(powers) == 0:
            return False
    
        cands = []
        i = 0
        while i < len(powers) and powers[i] < n:
            if powers[i] == n:
                return True
            i += 1
    #    print("i="), i
        if i != len(powers):
            cands.append(i)
        if i:
            cands.append(i-1)
    
        for c in cands:
            d = abs(powers[c] - n)
            if d < n:
                if myfind(d, powers[:c] + powers[c+1:]):
                    return True
        return False
    
    print("YES") if myfind(n, powers) else "NO"