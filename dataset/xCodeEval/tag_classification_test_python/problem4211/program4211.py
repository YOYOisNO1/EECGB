def program4211():
    s = input()
    ok = "CODEFORCES"
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            if s[:i]+s[j:] == ok:
                print("YES")
                exit(0)
    print("NO")