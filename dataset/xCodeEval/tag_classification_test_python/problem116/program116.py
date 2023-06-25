def program116():
    n = int(input())
    s = input()
    flag=0
    for i in range(n):
        if i==0:
            if s[0] == '?':
                flag=1
                break
        elif i==n-1:
            if s[n-1] == '?':
                flag=1
                break
        else:
            if s[i] == '?':
                if s[i-1] == s[i+1]:
                    flag=1
                    break
                if s[i-1]=='?' or s[i+1]=='?':
                    flag=1
                    break
    for i in range(n-1):
        if s[i] == s[i+1] and s[i] != '?':
            flag=0
    if flag==0:
        print('No')
    else:
        print('Yes')