    n=int(input())
    inst=[]
    
    for i in range(0,n):
        inst.append(input())
    
    ok=True
    instN=0
    NL=0
    i=0
    
def dchar(dirstr):
        if dirstr.find("South")>0:
            return "S"
        elif dirstr.find("East")>0:
            return "E"        
        elif dirstr.find("West")>0:
            return "W"        
        elif dirstr.find("North")>0:
            return "N"        
    
def dnum(dirstr):
        return int(dirstr[:dirstr.find(" ")])
            
    
    while ok and instN<n:
        if NL==0 and dchar(inst[instN])!="S":
            ok=False
        elif NL==20000 and dchar(inst[instN])!="N":
            ok=False
        
        if (dchar(inst[instN])=="S") and ok:
            NL+=dnum(inst[instN])
            
        elif (dchar(inst[instN])=="N") and ok:
            NL-=dnum(inst[instN])
            
        if NL>20000 or NL<0:
            ok=False
            
        instN+=1
         
    if NL==0 and ok:
        print("YES")
    else:
        print("NO")
        
    #print("kol2",kol2)