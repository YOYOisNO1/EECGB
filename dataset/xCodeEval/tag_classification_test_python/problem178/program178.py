    t=input()
    s=""
    for i in range(len(t)):
        if((t[i]=="Q")or (t[i]=="A")):
            s=s+t[i]
    tab=[1]
    v=s.find("Q")
    u=[]
    comp=1
    for i in range(v+1,len(s)):
        if(s[i]==s[i-1]):
            comp=comp+1
            tab.append(comp)
        else:
            u.append(comp)
            comp=1
            tab.append(comp)
    if(i<len(s)):
        if (s[i]=='Q'):
            u.append(comp)
def g(l,i):
        s=0
        for j in range(i,len(l),2):
            s=s+l[j]
        return s       
def f(l):
        s=0
        for i in range(0,len(l)-1,2):
            for j in range(i+1,len(l)-1,2):
                s=s+l[i]*l[j]*g(l,j+1)
                
        return s
    print(f(u))
                
            
    