def ftot(a):
        x = 0
        y = 0
        while a > 0:
            b = a % 10
            y += b * (3**x)
            x += 1
            a //= 10
        return y
    
def ttof(a, x):
        if a == '0':
            return ''
        return ttof(str(int(a) // 3), x+1) + str(int(a) % 3)
        
    r = input().split()
    a = ttof(r[0], 0)
    c = ttof(r[1], 0)
    if a == '':
        a = '0'
    if c == '':
        c = '0'
    while len(c) < len(a):
        c = '0' + c
    while len(a) < len(c):
        a = '0' + a
    b = ''
    for x in range(len(a)):
        l = (int(c[x]) % 3 - int(a[x]) % 3) % 3
        b += str(l)
    b = ftot(int(b))
    print(b)