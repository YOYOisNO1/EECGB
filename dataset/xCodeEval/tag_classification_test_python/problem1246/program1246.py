def program1246():
    input()
    s = input()
    a = [[0, 0] for i in range(len(s))]
    for i in range(len(s)):
        a[i] = a[i-1].copy()
        if s[i] == "0":
            a[i][0] += 1
        else:
            a[i][1] += 1
    
    k0 = a[len(s)-1][0]
    k1 = a[len(s)-1][1]
    if k0 == k1:
        print(2)
        print(s[:len(s)-1], s[len(s)-1])
    else:
        print(1)
        print(s)