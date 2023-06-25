def program1249():
    a = [int(x) for x in input().split(' ')]
    q, w, r = a[0], a[1], a[2]
    c = min(q, w)
    ans = 2 *( r + c)
    If q > c:
        ans += 1
    If w > c:
        ans += 1
    print(ans)