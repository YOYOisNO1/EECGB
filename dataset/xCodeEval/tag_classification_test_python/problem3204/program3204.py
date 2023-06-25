def program3204():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 0
    i = 1
    while i < n:
        ans+=(a[i]-a[i-1])
        i+=2
    print(ans)    