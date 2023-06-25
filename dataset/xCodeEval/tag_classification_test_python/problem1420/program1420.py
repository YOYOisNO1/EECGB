def program1420():
    n,k=(int(x) for x in input().split(" "));
    
    m=2;
    count=0;
    list=[];
    while(n>=m and count<k-1):
        p=n%m;
        if(p==0):
            list.append(m);
            count=count+1;
            n=n//m;
        else:
            m=m+1;
         
    if(count==k-1 and n!=1):
        for i in range(0,k-1):
            print(list[i],end=" ");
        print(n);
    else:
        print(-1);