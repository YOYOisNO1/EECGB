def program1080():
    n, k = map(int, input().strip().split())
    a = map(int, input().strip().split())
    
    ka = 0
    et = [[0 for j in range(n/k)] for i in range(k)]
    
    for i in range(k):
        for j in range(n/k):
            et[i][j] = a[i+k*j]
    
    for i in range(k):
        if len(set(et[i])) > 1:
            ka = ka + min(et[i].count(1), et[i].count(2))
    
    print(ka)