def program784():
    [a, b] = map(int, input().split())
    map = [6,  2,  5,  5, 4, 5, 6, 3, 7, 6]
    ans = 0
    
    for numb in range(a, b + 1):
        for c in list(str(numb)):
            ans += map[int(c)]
    
    print(ans)