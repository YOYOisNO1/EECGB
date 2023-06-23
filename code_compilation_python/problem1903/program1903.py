    b=input().split()
    a1=input().split()
    a2=input().split()
    a=int(a1[0])
    b=int(a1[1])
    c=int(a2[0])
    d=int(a2[1])
    e=int(b[0])
    f=int(b[1])
    
def fitsin(a1,a2,b1,b2):
        return max(b1,b2)<=max(a1,a2) and min(b1,b2)<=min(a1,a2)
    
    if fitsin(f-a,e,c,d) or fitsin(e-b,f,c,d) or fitsin(f-b,e,c,d) or fitsin(e-a,f,c,d):
        print("YES")
    else:
        print("NO")