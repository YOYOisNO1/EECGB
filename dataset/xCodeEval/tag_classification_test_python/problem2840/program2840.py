def program2840():
    l=lambda: map(int,input().split())
    n=input()
    s=input()
    ans=list(s)
    half=n/2
    cnt=0
    i=0
    while i<n:
        x=ans.count('x')
        if x==half:
            break
        elif x<half:
            if ans[i]=='X':
                ans[i]='x'
                cnt+=1
        else:
            if ans[i]=='x':
                ans[i]='X'
                cnt+=1
        i+=1
    print(cnt)     
    print('').join(ans)