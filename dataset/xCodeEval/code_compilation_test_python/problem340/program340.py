def program340():
    n=input()
    p=''
    bv=0
    if len(n)%2==0:
        for i in range(len(n)//2):
            u=n[len(n)-1-i]+n[i]
            p+=u
    elif len(n)%2!=0:
        if len(n)>1:
            for j in range(len(n)//2):
                u=n[i]+n[len(n)-1-i]
                p+=u
            p+=n[(len(n)//2)+1]
        else:
            print(n)
            bv+=1
    
    if bv==0:
        z=''
        for k in range(len(n)-1,-1,-1):
            z+=p[k]
        print(z)
    
            