def program2046():
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        for j in range (i,n+1):
            if i^j <= n and i^j>j and i+j>i^j:
                sum += 1
    print(sum)