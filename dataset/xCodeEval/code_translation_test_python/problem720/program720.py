def program720():
    n = int(input())
    count = 0
    for i in range(1,n):
        for j in range(i+1,n+1):
            k = i^j
            if k>i and k>j:
                if k <=n and k < i+j:
                    count += 1
    
    print(count)