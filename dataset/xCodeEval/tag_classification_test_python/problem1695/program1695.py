def program1695():
    n=int(input());i=0;a=[]
    while(n!=1):
        i+=1
        if n%2:a.insert(0,i)
        n=n//2
    print(i+1,*a)