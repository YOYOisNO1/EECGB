def program1717():
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]
    for i in range(len(a)-1,-1,-1):
        if a[i] not in ans:
            ans.append(a[i])
        else:
            pass
    ans=ans[::-1]
    print(len(ans))
    print(*ans)