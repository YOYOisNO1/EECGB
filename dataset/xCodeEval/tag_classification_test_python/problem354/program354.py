def program354():
    import math
    p,r=map(int,input().split())
    k=1
    count=1
    while(1):
        n=(p*k-r)/10
        nwr=p*k/10
        if(n==int(n)or nwr==int(nwr)):
            print(count)
            break
        k+=1
        count+=1