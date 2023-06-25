def program1698():
    f,q=[0]*99,0
    a,b,c=map(int,input().split())
    for i in range(a):
        s=input()
        for j in range(b):
            if s[j]=='Y':f[j]+=1
                if f[j]==c:q+=1
    print(q)#kitten