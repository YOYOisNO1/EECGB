def program4401():
    s=input()
    if s[:3]=="dot" or s[:2]=="at" or s[len(s)-2:]=="at" or s[len(s)-3:]=="dot":
        if s[:3]=="dot":
            t=s[3:]
            a=t.split('dot')
            l=".".join(a)
            b=l.find("at")
            o=l[:b]+"@"+l[b+2:]
            q="dot"+o
            if q[-1]==".":
                a=q[:len(q)-1]
                s=a+"dot"
            elif q[-1]=="@":
                a=q[:len(q)-1]
                s=a+"at"
            else:
                s=q
    
        if s[:2]=="at":
            t=s[2:]
            a=t.split('dot')
            l=".".join(a)
            b=l.find('at')
            o=l[:b]+"@"+l[b+2:]
            q="at"+o
            if q[-1]==".":
                a=q[:len(q)-1]
                s=a+"dot"
            elif q[-1]=="@":
                a=q[:len(q)-1]
                s=a+"at"
            else:
                s=q
    
        if s[len(s)-3:]=="dot" and s[:3]!="dot" and s[:2]!="at":
            t=s[:len(s)-3]
            a=t.split('dot')
            l=".".join(a)
            b=l.find('at')
            q=l[:b]+"@"+l[b+2:]
            s=q+"dot"
    
        if s[len(s)-2:]=="at" and s[:3]!="dot" and s[:2]!="at":
            t=s[:len(s)-2]
            a=t.split('dot')
            l=".".join(a)
            b=l.find('at')
            q=l[:b]+"@"+l[b+2:]
            s=q+"at"
    
    
        print(s)
    
    else:
        a=s.split('dot')
        l=".".join(a)
        b=l.find('at')
        q=l[:b]+"@"+l[b+2:]
        print(q)