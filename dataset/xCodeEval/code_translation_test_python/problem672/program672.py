def program672():
    n=int(input())
    count=0
    i=1
    
    for i in range(1,n):
    
        if n%i==0:
            count+=1
        i+=1
    
    print(count)