def program256():
    n=int(input())
    d,c,m,i=0,1,1,1
    while c<=n:
        d+=1
        i+=1
        m+=i
        c+=m
    print(d)