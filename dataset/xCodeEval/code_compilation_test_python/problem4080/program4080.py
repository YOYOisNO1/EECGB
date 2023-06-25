def program4080():
    s = input()
    a = s.split()
    #print a
    v1 = a[0]
    v2 = a[1]
    s = input()
    a = s.split()
    t = int(a[0])
    d = a[1]
    sum = 0
    for i in range(t):
        sum += min(v1 + i * d, v2 + (i-t) * d)
    print sum