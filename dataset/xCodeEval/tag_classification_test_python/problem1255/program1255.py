def program1255():
    n = input()
    a=0;b=0;ans=0
    for i in range(n):
        l,r = map(int,input().split())
        a += l
        b += r
        if((l+r)%2==1):
            ans=1
    if((a+b)%2==1):
        print(-1)
    elif a%2==0 and b%2==0:
        print(0)
    elif ans == 0:
        print(-1)
    else:
        print(1)