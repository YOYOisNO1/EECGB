def program3007():
    n, k, x = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
    
    for i in range(-1, (-1*n)-1, -1):
        if k != 0:
            ans += x
            k -= 1
        else:
            ans += l[i]
    
    print(ans)