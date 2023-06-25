def program3641():
    s = input()
    ans = -1
    for i in range(1,len(s)):
        for j in range(i+1, len(s)):
            a = s[:i]
            b = s[i:j]
            c = s[j:]
            if (a[0]!='0' or int(a)==0) and (b[0]!='0' int(b)==0) and (c[0]!='0' or int(c)==0) and int(a)<=1000000 and int(b)<=1000000 and int(c)<=1000000:
                ans = max([ans, int(a)+int(b)+int(c)])
    print ans