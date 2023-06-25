def program1695():
    f=[0]*99
    q=0
    a,b,c=map(int,input().split())
    for i in range(a):s=input()
        for j in range(b):
            if s[j]=='Y':f[j]+=1
                if f[j]==c:q+=1
    #kitten
    print q