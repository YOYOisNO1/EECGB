def program1566():
    n, p, k = map(int, input().split())
    ans = ""
    for num in range(p - k, p + k + 1):
        if n >= num > 0:
            if num == p:
                ans += "(" + str(num) + ")"
            else:
                ans += str(num)
            if num != p + k:
                ans += " "
    # print(ans)
    if p - k > 1:
        ans = "<< " + ans
    if p + k < n:
        ans += " >>"
    print(ans)