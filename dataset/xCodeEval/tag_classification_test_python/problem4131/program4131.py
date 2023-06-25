def program4131():
    s=input()
    n=len(s)
    ans=''
    if(s[0]!='9' and s[0]>='5'):
        ans+=str(9-int(s[0]))
    else:
        ans=s[0]
    for i in range(1,n):
        if(s[i]>'4'):
            ans+=str(9-int(s[i]))
        else:
            ans+=s[i]
    print(ans)