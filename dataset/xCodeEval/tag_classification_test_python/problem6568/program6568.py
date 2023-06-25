def program6568():
    n,t = (int(e) for e in input().split())
    a = []
    for i in range(n):
        b = []
        for j in range(i+1):
            b.append(0)
        a.append(b)
    
    current_row = 0
    for x in range(t):
        for i in range(n):
            for j in range(i+1):
                if i == 0:
                    a[i][j] += 1
                if a[i][j] > 1 and i+1 < n and j < 10:
                    a[i+1][j]+=(a[i][j]-1)/2
                    a[i+1][j+1]+=(a[i][j]-1)/2
                    a[i][j] = 1
                if a[i][j] > 1 and i==n-1:
                    a[i][j] = 1
    #print(a)
    count = 0
    for i in range(n):
        for j in range(i+1):
            if a[i][j] == 1:
                count += 1
    print(count)