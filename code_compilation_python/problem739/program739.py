def program739():
    n=int(input(""))
    p=n s=0 t=1 i=0
    while p<10:
        i+=1
        s+=(i*9*t)
        t*=10
        p=p/10
    n=n-math.pow(10,i)+1
    print s+n*(i+1)