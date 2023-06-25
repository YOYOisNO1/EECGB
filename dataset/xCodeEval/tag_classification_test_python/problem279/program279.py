def program279():
    #In The Name Of God
    
    n=int(input());
    ind1=0;indn=0;
    a=input().split();
    for i in range(0,n):
        x=int(a[i]);
        if x==1:
            ind1=i;
        elif x==n:
            indn=i;
    print(max(n-1-ind1,ind1,n-1-indn,indn));