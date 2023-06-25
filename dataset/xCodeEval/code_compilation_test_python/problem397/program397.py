def program397():
    x = input().split()
    ans = 0
    for i in range(61):
        for j in range(i - 1):
            y = 2 ** i - 1 - 2 ** j
            if y >= x[0] and y <= x[1]:
                ans++
    print(ans)