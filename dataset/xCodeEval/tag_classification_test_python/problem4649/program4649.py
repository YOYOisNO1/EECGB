    gates={}
    state_gates={}
    
def main(n,l,gates,state_gates,guards): #str,str int
        for i in range(n):
            gate=l[i]
            if state_gates[gate]!=True:
                if guards>0:
                    state_gates[gate]=True
                    guards-=1
                else:
                    return "YES"
            
            if gates[gate][1]==i:
                state_gates[gate]=False
                guards+=1
        else:return "NO"
    
    g=input().split()
    guards=int(g[1])
    l=input()
    n=int(g[0])
    for i in range(n):
        if gates.has_key(l[i]):gates[l[i]][1]=i
        else:gates[l[i]]=[i,i]
        
        state_gates[l[i]]=False   #True=open   False=close
    
    print(main(n,l,gates,state_gates,guards))