def program1578():
    n=int(input())
    a=map(int,input().split())
    ans=0
    flag=False
    for i in range(n-1):
        if a[i] != 1 and a[i+1] != 1:
            flag=True
        elif a[i] == 2 or a[i+1] == 2:
            ans+=3
        elif a[i] == 3 or a[i+1] == 3:
            ans+= +=4
    if flag:
        print("Infinite")
    else:
        print(ans)
    
            