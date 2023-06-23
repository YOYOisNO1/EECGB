def program1713():
    s=str(input())
    d={}
    p=1
    for i in range(0,len(s)):
        if(s[i]=='0'):
            d[s[i]]=2
        elif(s[i]=="1"):
            d[s[i]]=
        elif(s[i]=="8"):
            d[s[i]]=1
        elif(s[i]=="9"):
            d[s[i]]=2 
        elif(s[i]=="2"):
            d[s[i]]=2
        elif(s[i]=="3"):
            d[s[i]]=3
        
        elif(s[i]=="4"):
            d[s[i]]=3
        elif(s[i]=="5"):
            d[s[i]]=4 
        elif(s[i]=="6"):
            d[s[i]]=2
        elif(s[i]=="7"):
            d[s[i]]=5    
    for k,v in d.items():
        p=p*(d[k])
    if(s[0]==s[1]):
        print(p*p)
    else:
        
        print(p)
        