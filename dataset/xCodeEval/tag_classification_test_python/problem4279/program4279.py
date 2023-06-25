def program4279():
    len = int(input(""))
    str = input("")
    ans = ""
    flg = False
    for i in range(0,len):
        if str[i] in "aeiouy":
            if flg == False:
                ans += str[i]
            flg = True
        else:
            ans += str[i]
            flg = False
    print(ans)