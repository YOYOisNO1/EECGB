def program3848():
    n = int(input().strip())
    a = map(int, input().strip().split())
    a = [0] + a + [0]
    i = 1
    r = 0
    while i <= n:
        if a[i-1] == 0 and a[i] == 3:
            j = i
            while i <= n and a[i] == 3:
                i += 1
            if i == n+1:
                break
        else:
            if a[i] == 3:
                a[i] = 3-a[i-1]
            elif a[i] == a[i-1]:
                a[i] = 0
    
        i += 1
    a = a[1:n+1]
    print(a.count(0))