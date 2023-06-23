def mp():
        return map(int, input().split())
    
    s = input() + '+'
    r = 0
    a = 0
    z = '+'
    for i in s:
        #print(r, a, z)
        if i in '+-':
            if z == '+':
                r += a
            else:
                r -= a
            z = i
            a = 0
        a *= 10
        a += ord(i) - ord('0')
        
    print(r)