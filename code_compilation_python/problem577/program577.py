def program577():
    n = int(input())
    s = input()
    ans = 0
    while s:
        if len(s) % 2 == 1:
            ans += 1
            s = s[:len(s) - 1]
        else:
            if s[:len(s) // 2] == s[len(s) // 2:]:
                ans += 1
                s = s[:len(s) // 2]
            else:
                ans += 1
                s = s[:len(s) - 1]
    print(ans)