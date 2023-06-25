def program700():
    a,b=map(int,input().split())
    s=(a)*(a+1)//2
    k=b%s
    p=0
    i=0
    while (p+i)<=k :
        p+=i
        i+=1
    print(k-p)