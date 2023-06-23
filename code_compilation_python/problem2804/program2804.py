def program2804():
    n, m, k = map(int, input().split())
    l = [int(i) for i in input().split())]
    m -= 1
    ans = []
    for j in range(n):
        if l[j] !=0 and l[j]<=k:
            ans+=[abs(j - m)*10]
    print(min(ans))