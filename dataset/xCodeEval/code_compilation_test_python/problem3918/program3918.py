def program3918():
    a=[int(i) for i in (input().split())]
    f,sm=[0,1,1],[0]
    s=a[0]
    k=a[1]
    ssum=0
    while ssum<s :
        i=k+2
        sumi=1
        while sumi<=s-ssum :
            sumi=sumi+f[i-k]
            i=i+1
            if ssum==0 :
                f.append(2*f[i-k-1])
                if i-k-(k+1)>=0 :
                    f[i-k]=f[i-k]-f[i-k-(k+1)]
        ssum=ssum+f[i-k-1]
        sm.append(f[i-k-1])
    print(len(sm))
    for i in range(0,len(sm)-1):
        print( sm[i] , end = " " )
    print(sm[len(sm)-1])
    