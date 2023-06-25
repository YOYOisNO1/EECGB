def program1496():
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    if a==b:print(0)
    else:
        M,u=2*a*b,0
        D=1
        while D*D<=b-a:
            if (b-a)%D==0:
                for d in (D,(b-a)//D):
                    k=0
                    if a%d!=0:
                        k=d-a%d
                    Q=(a+k)*(b+k)/d
                    if Q<M:
                        M=Q
                        u=k         
            D+=1
        print(u)
        