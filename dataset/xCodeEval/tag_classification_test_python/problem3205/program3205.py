def program3205():
    n=input()
    l=list(map(int,input().split()))
    l.sort()
    i=0
    j=1
    s=0
    while(j<n):
       s=s+l[j]-l[i]
       i=i+2
       j=i+1
    print(s)