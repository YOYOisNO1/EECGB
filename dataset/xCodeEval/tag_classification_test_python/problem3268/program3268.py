def program3268():
    n=int(input())
    s=list(input())
    k=0
    d=''
    for i in range(n):
        if s[i]=='1':
            k+=1
        else:
            d=d+str(k)
            k=0
        #print(d)
    d=d+str(k)
    print(d)
    