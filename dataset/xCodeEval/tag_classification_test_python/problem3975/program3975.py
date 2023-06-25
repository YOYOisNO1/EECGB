def program3975():
    w,m=map(int,input().split())
    tmp=m
    ar=[]
    while tmp:  
        ar.append(tmp%w) #converting to base w
        tmp=tmp//w
    flag = True
    l=len(ar)
    car=0 #signifies carry of previous addition
    for i in range(0,l):
        s=(ar[i]+car)%w
        car=(ar[i]+car)//w
        if s==0: 
            continue #entry is 0 skip
        elif s==1:
            continue #entry is 1 skip
        elif s==w-1:
            #we can make this 0 by adding 1 here
            car=1 
            continue
        else:
            flag=False #not possible to make it all 1's and 0's
            break
    print("YES") if flag else "NO" 