def program2791():
    R = lambda:map(int,input().split())
    
    
    n, = R()
    li = [0] * (n+1)
    
    for i in range(2, (n//2) + 1):
        if li[i] == 0:
            for j in range(i*2, n+1, i):
                li[j] += 1
    
    print(li.count(2))