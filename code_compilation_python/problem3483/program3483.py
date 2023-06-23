def program3483():
    a=input()
    total=1
    ans=0
    for i in range(len(a)):
        if i+1<len(a)&&a[i]==a[i+1]:
            total+=1
        else:
            if total%2:
                ans+=1
            total=0
    print(ans)