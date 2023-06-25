def program855():
    k=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a.reverse()
    tot=sum(a)
    d=0
    n=0
    for i in range (len(a)):
        tot=tot-a[i]
        d=d+a[i]
        n=n+1
        if k==0:
            print("0")
            break
        elif d==k or d>k:
            print(n)
            break
         elif d<k:
             print("-1")
             break
            
        
        
        