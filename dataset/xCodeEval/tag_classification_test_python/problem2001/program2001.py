def program2001():
    s = str(input())
    n = int(s.split()[0])
    k = int(s.split()[1])
    d = int(s.split()[2])
    
    # total (with & without >= d)
    array = [0] * 105
    array[0] = 1
    for i in range(1, n+1):
        for j in range(1, min(k, i) + 1):
            array[i] = (array[i] + array[i-j]) % 1000000007
    
    # complement (without >= d)
    brray = [0] * 105
    brray[0] = 1
    
    for i in range(1, n+1):
        for j in range(1, min(k, i, d-1) + 1):
            brray[i] = (brray[i] + brray[i-j]) % 1000000007
    
    print((array[n] - brray[n]) % 1000000007)
    