def program1500():
    l1, r1, l2, r2, k = map(int, input().split())
    ans = 0
    if l1 >= l2 and r1 <= r2:
        ans = r1 - l1 + 1
        if l1 <= k <= r1:
            ans -= 1
    elif l2 >= l1 and r2 <= r1:
        ans = r2 - l2 + 1
        if l2 <= k <= r2:
            ans -= 1
    elif l1 >= l2 and r2 >= l1:
        ans = r2 - l1 + 1
        if l1 <= k <= r2:
            ans -= 1
    elif l1 < l2 and l2 <= r1:
        ans = r1 - l2 + 1
        if l2 <= k <= r1:
            ans -= 1
    print(ans)