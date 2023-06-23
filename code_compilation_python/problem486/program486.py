def program486():
        n,a,b,c=map(int,input().split())
        x=sorted([a,b,c])
        if n>sum(x):
            print(n)
        else:
            c=0
            for i in x:
                if i<=n:
                    c+=1
                    n-=i
            print(c)