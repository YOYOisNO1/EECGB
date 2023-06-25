def program1431():
    n = input()
    total = sum(map(int, input().split()))
    ans = 0
    for i in xrange(1, 6):
        if (total+i)%(n+1) != 1:
            ans += 1
    print(ans)