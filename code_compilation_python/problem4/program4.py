def program4():
    n = int(input())
    ans = float("+inf")
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i*j >= n:
                ans = min(ans, (i+j)*2)
    print(ans)