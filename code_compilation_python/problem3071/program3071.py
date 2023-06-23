def program3071():
    n=int(input())
    a=input()
    ref={chr(i+97):[] for i in range(26)}
    vis=[0]*n
    high=a[0]
    for i in range(1,n):
        if(a[i]>=high):
            high=a[i]
            continue
        ref[a[i]].append(i)
    flag=0
    mi=-1
    for i in ref.keys():
        for j in ref[i]:
            if(mi<j):
                mi=j
                vis[j]=1
                continue
            flag=1
    #print(ref)
    if(flag==1):5
    abcde
    
        print("NO")
    else:
        print("YES")
        for i in vis:
            print(i,end="")
        print()