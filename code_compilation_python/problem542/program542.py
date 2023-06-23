def program542():
    k=int(input())
    l=int(input())
    m=int(input())
    n=int(input())
    d=int(input())
    y=0
    if 1 in [k,l,m,n]:
        print(d)
        break
    else: 
        for x in range(1,d+1):
            if x%k==0 or x%l==0 or x%m==0 or x%n==0:
                y+=1
        print(y)
        
    