def program2904():
    
    s=input()
    a={"R","G","B","Y"}
    l=list(s)
    dict={}
    if(s.__contains__("!")==False):
        print(0,0,0,0)
    else:
        for e,f in enumerate(l):
            if e%4 not in dict and f!="!":
                dict[e%4]=f
        n={}
        for i in range(len(s)):
            if(s[i]=="!"):
                if  dict[i%4] not in n:
                    n[dict[i%4]]=1
                else:
                    n[dict[i%4]]+=1
        b=set()
        for e in n.keys():
            b.add(e)
        s=a.difference(b)
        for e in s:
            n[e]=0
        print(n["R"],n["B"],n["Y"],n["G"])