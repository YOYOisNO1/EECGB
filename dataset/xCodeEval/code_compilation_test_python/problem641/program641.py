def func(n):
        if n[0]%4==1:return (min(n[3],n[1]*3,n[2]+n[1]))
        elif n[0]%4==2:return (min(n[2],n[3]*2,n[1]*2))
        elif n[0]%4==3:return (min(n[1],n[2]+n[3])
        else:return 0
    print(func(list(map(int,input().split()))))