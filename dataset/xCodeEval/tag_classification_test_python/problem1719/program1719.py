def program1719():
    n=input()
    num=input()
    num=num.split()
    ans=''
    count=0
    for  l in range(int(n)):
        if num[l] in num[l+1:]:
            continue
        else:
            count=count+1
            ans=ans+' '+num[l]
    print(count)
    print((ans.lstrip()))