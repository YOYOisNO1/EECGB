def program553():
    n=int(input())
    l=input().split()
    l=list(map(int,l))
    z=0
    for i in range(len(l)):
        z=z+i*l[i]
    k=(len(l)-1)*(len(l)-2)/2
    x=int(z/k)
    
    f=(sum(l)-l[0])
    ab=0
    for i in range(1,len(l)):
        ab=ab+abs(i-x)
    
    print(2*z+f+ab)
    
    
    
    
    
    
    
    