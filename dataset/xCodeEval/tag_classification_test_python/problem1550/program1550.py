def program1550():
    m=input("")
    
    
    c1=input("").split()  
    c=[int(j) for j in c1]
    
    lim1=input("").split()  
    lim=[int(j) for j in lim1]
    
    p1=0
    
    this=0
    
    k1=0
    
    if sum(c)>lim[1]*2: #and sum(c)<lim[0]*2:
        print("0")
        k1=1
    else:
        for i in range(len(c)-1,-1,-1):
            p1+=c[i]
            this=i
            if p1>lim[1]:
                p1-=c[i]
                this=i+1
                break
            if sum(c)-p1<lim[0]:
                p1-=c[i]
                this=i+1
                break
            
        if this+1>len(c):
            print("0")
            k1=1
        elif lim[0]<=p1<=lim[1]:
            if lim[0]<=sum(c)-p1<=lim[1]:
                print(this+1)
            else:
                print("0")
                k1=1
        
        elif k1!=1 and p1==0:
            print("0")
        else:
            print("0")
            k1=1
        
            
    
    
            