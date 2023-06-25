def program570():
    n,l,r=map(int,input().split())
    x=1
     
    sum1=0
    sum2=0
     
    for i in range(l) :
        sum1+=x
        x=x*2
    for i in range(n-l) :
        sum1+=1
     
    x=1
    for i in range(r) :
        sum2+=x
        x*=2
    x=x//2
     
    for i in range(n-r) :
        sum2+=x
    print(sum1,sum2,sep=" ")