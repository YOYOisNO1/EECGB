def program3020():
    a,ans,x=input(),-1,[]
    for i in a:
        y=x[:]
        for t in y:
            m=t*10+int(i)
            if ceil(m**.5)==int(m**.5):
                if ans <m:ans=m
            x.append(m)
        if i!='0':
            i=int(i)
            if ceil(i**.5)==int(i**.5):
                if ans <i:ans=i
            x.append(int(i))
        
    print(ans if ans==-1 else len(a)-len(str(ans)))
    
            
    
            