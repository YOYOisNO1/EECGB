def program3795():
    n = int(input())
    m = str(n)
    if n > 0:
        print(n)
    if n < 0:
        x = m[len(m) - 1]
        y = m[len(m) - 2]
        a = int(m[-1::-1].replace(x, '', 1)[-1::-1])
        b = int(m[-1::-1].replace(y, '', 1)[-1::-1])
        z = max(a, b)
    
        print(z)
    
    
    