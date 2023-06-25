def program372():
    n,a=map(int,input().split())
    if(n==1):
        print(int(input()))
    else:
        l=list(map(int,input().split()))
        if(a==1 or a==n):
            print(l.count(1))
        else:
            c=0
            i=a-1
            if(l[i]==1):
                c+=1
            f=i-1
            b=i+1
            while(1):
                if(l[f]==1 and l[b]==1):
                    c=c+2
                if(i-f!=b-i):
                    if(l[f]==1 or l[b]==1):
                        c=c+1
                if(f==0):
                    if(b==n-1):
                        break
                if(f>0):
                    f=f-1
                else:
                    l[f]=0
                if(b<n-1):
                    b=b+1
                else:
                    l[b]=0
                
            print(c)