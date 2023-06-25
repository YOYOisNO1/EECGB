def program4994():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[7,6,5,4,3,2]
        x=0
        i=0
        while(i<6 and n>0 ):
            if n<a[i]:
                i+=1 
            else:
                c=n%a[i]
                x+=n//a[i]
                n=c
        if n==1:
            x+=1
        print(x)        
            