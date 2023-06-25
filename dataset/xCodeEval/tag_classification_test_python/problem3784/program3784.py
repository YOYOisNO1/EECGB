def program3784():
    #IN THE NAME OF ALLAH
    
    #variables
    n=int(input())
    n=n*2
    s=input()
    s=[int(m) for m in s]
    
    #solve
    s[0:int(n/2)]=sorted(s[0:int(n/2)],reverse=True)
    s[int(n/2):n]=sorted(s[int(n/2):n],reverse=True)
    
    #check
    #print(s)
    flag1=True;flag2=True
    for i in range(0,int(n/2)):
        if(s[i]>=s[i+int(n/2)]):
            flag1=False
        if(s[i]<=s[i+int(n/2)]):
            flag2=False
        if(flag1 or flag2): continue
        else: break
    
    #output
    if(flag2 or flag1): print("YES")
    else: print("NO")