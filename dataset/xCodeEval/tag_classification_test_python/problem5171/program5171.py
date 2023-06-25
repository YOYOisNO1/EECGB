def program5171():
    n,l,r=map(int,input().split())
    mu = []
    while n > 1:
        mu.append(n%2)
        n = n /2
    mu.append(n)
    ans = 0
    s = ''
    for i in range(l-1,r) :
        s = "0" + bin(i)[2:]
        tmp = 1
        while s[-tmp] != "0":
            tmp += 1;
        ans += mu[-tmp]
    print(ans)