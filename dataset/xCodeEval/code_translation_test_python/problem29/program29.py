def program29():
    n = int(input())
    s = input();
    cnt1 = 0
    cnt2 = 0
    s1 = ""
    for i in range(1, n):
        if s[i-1] == "S" and s[i] == "F":
            cnt1 += 1
        elif s[i-1] == "F" and s[i] == "S":
            cnt2 += 1
    if cnt1 > cnt2:
        print("YES")
    else:
        print("NO")