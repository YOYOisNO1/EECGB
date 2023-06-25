def program6020():
    a,b=map(int,input().split())
    l=[0]*3
    for i in range(1,7):
        if abs(a-i)<abs(b-i):l[0]+=1
        else:l[2if abs(a-i)>abs(b-i)else 1]+=1
    print(*l)