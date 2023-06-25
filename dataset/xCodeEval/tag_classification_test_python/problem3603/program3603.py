def program3603():
    n,m=map(int,input().split())
    o=list(input())
    for t in range(m):
        i=1
        while i<n:
            if o[i-1]=='B' and o[i]=='G':
                o[i-1],o[i]=o[i],o[i-1]
                i+=1
            i+=1
    print(''.join(o))