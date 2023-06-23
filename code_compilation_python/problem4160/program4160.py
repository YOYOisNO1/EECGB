def program4160():
    n,m,s=map(int,input().split())
    
    n,m=min(n,m),max(n,m)
    if(s>=max(n,m)):
        print(n*m)
    elif(s>=n and s<m):
        x=1
        count=1
        while(1):
            if(x+s<=m):
                x+=s
                a1+=1
            else:
                break;
        print(a1*n)
        
    else:
        a1=1
        x=1
        y=1
        a2=1
        while(1):
            if(x+s<=m):
                x+=s
                a1+=1
            else:
                break;
        while(1):
            if(y+s<=n):
                y+=s
                a2+=1
            else:
                break;
        print(a1*a2*(m%s)*(n%s))
       