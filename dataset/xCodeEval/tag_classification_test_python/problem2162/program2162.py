def program2162():
    n=list(input())
    ans=''
    if n[0]=='h':
        n=n[4:]
        ans+='http://'
    else:
        n=n[3:]
        ans+='ftp://'
    chk=1
    while 1:
        if n[chk]=='r' and n[chk+1]=='u':
            ans+=(''.join(n[0:chk])+'.ru/'+''.join(n[chk+2:]))
            break
        else:
            chk+=1
    print(ans) if ans[-1:]!='/' else ans[:-1]