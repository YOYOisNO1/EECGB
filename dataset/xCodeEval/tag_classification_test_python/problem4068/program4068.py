def program4068():
    import string
    
    s = input()
    l = len(s)
    i = 0
    ans = ""
    
    while(i+2<=l-1):
        if s[i:i+3]=="WUB":
            i += 3
        else:
            while(i+2<=l-1 and s[i:i+3]!="WUB"):
                ans += s[i]
                i += 1
            if i+2<=l-1:
                ans += " "
    if i+2>l-1:
        ans += s[i:l]
    print(ans)
    
    