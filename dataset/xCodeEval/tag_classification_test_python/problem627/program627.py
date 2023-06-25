def program627():
    list = [0 for x in range(26)]
    trash = input()
    s = input()
    
    ans = 0
    for c in s:
        int_c = ord(c) - ord('a')
        if int_c >= 0 and int_c < 26:
            list[int_c] = 1
        else:
            for i in range(26):
                list[i] = 0
        tmp = 0
        for i in list:
            tmp += i
        ans = max(ans, tmp)
    
    print(ans)