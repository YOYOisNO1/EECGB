def program3303():
    n=int(input())
    
    small,tmp,d=1,n,2
    while tmp>1:
        if tmp%d==0:
            small*=d
            while tmp%d==0: tmp//=d
        d+=1
    
    tmp,k=small,0
    while tmp%n>0:
        tmp*=tmp
        k+=1
    if tmp>n:k+=1
    
    print(small,k)
    