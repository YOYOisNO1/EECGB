def program470():
    n = int(input())
    l =[0]+ list(map(int,input().split()))
    l.append(1001)
    #print(l)
    m,c = 1,0
    for i in range(1,n+2):
        if l[i]-l[i-1]==1:
            c+=1
        else:
            m=max(m,c)
            c=0
    m = max(m,c)
    print(m-1)