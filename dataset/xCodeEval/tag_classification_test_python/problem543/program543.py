def program543():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    ans = [1, 2, 3]
    for i in range(n):
        if a[i] == ans[2]:
            print("NO")
            break
        if ans[1] == a[i]:
            ans[0], ans[2] = ans[2], ans[0]
        else:
            ans[1], ans[2] = ans[2], ans[1]
        if i == n - 1:
            print("YES")