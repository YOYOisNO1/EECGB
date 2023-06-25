def program6317():
    n1,n2 = map(int,input().split());
    
    if(n2-n1)>10:
        print((0);)
    else:
        result=1;
        for i in range(n1+1,n2+1):
            result*=i;
        print((result%10);)