def program813():
    n=int(input())
    if n<10:
        print(n)
        exit()
    chk=n
    ans=0
    c=[]
    for i in range(9,0,-1):
        c.append(10**i)
    for i in c:
        if chk>i-1:
            k=chk-(i-1)
            ans+=(k*(len(str(i))))
            chk-=k
    print(ans+9)