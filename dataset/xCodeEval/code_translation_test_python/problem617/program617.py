def program617():
    s = input()
    num = 0
    n = len(s)
    ans = ["YES","NO"]
    for i in range(n):
        num += int(s[i] != s[n-1-i])
    
    if num == 2:
        print(ans[0])
    elif num == 0 and n % 2 == 1:
        print(ans[0])
    else:
        print(ans[1])