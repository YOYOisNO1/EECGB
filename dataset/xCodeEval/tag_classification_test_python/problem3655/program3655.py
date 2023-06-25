def program3655():
    n,t=map(int,input().split())
    l=list(input())
    for _ in range(t):
        i=0
        while(i<n-1):
            if l[i]=='B' and l[i+1]=='G':
                l[i],l[i+1]=l[i+1],l[i]
                i+=1
            i+=1
    print("".join(l))
        