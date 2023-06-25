def program4492():
    s=input()
    bd=0
    for i in range((len(s)+1)/2):
        if s[i]==s[-i-1]:
            bd=bd+1
    if len(s)%2==1 and bd==(len(s)+1)/2:
        print('YES')
    elif bd==(len(s)+1)/2-1:
        print('YES')
    else:
        print('NO')