def program5998():
    m=list(map(int,input().split()))
    if sum(m)%2==1:
        print("NO")
    else:
        su=sum(m)//2
        p=0
        for i in set(range(6)):
            for j in set(range(6))-set([i]):
                for k in set(range(6))-set([i,j]):
                    if m[i]+m[j]+m[k]==su:
                        p=1
        print("YES") if p==1 else print("NO")