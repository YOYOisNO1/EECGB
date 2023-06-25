def func(a,n):
        b = ''
        lastchange = False
        for i in range(n):
            if lastchange:
                if a[i] == 'G':
                    b += 'B'
                    lastchange = False
                elif a[i] == 'B':
                    b += 'B'
            else:
                try:
                    if a[i] == 'B' and a[i+1] == 'G':
                        b += 'G'
                        lastchange = True
                    elif a[i] == 'G':
                        b += 'G'
                    elif a[i] == 'B' and a[i+1] == 'B':
                        b+= 'B'
                except:
                    b+= a[i]
        return b
                    
    n, t = map(int, input().split())
    a = input()
    b = a
    
    for j in range(t):
        b = func(b,n)
    print(b)
            