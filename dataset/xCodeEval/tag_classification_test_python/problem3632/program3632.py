def program3632():
    n,t=map(int,input().split())
    a=list(input())
    i=0
    for j in range(t):
        while i<n :
            if a[i:i+2]==['B','G']:
                a.pop(i+1)
                a.insert(i,'G')
                i+=1
            i+=1
        i=0
    for i in range(n):
        print(a[i],end='')