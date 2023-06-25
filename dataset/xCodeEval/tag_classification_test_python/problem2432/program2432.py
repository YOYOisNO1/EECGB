def program2432():
    value=int(input())
    string=input()
    string=string.lower()
    pam="abcdefghijklmnopqrstuvwxyz"
    outside=[]
    inside=[]
    count=0
    wait=0
    for it in string:
        if wait==0:
           if it=="_":
               outside.append(count)
               count=0
           elif it=="(":
               outside.append(count)
               count=0
               wait=1
           else:
               count+=1
        else:
            if it==")":
                wait=0
    outside.append(count)
    wait=0
    count=0
    sim=0
    for it in string:
        if it=="(":
            wait=1
        else:
            pass
        if wait==1:
            if it=="_":
                if count>0:
                    sim+=1
                    count=0
            elif it==")":
                if count>0:
                    sim+=1
                wait=0
                count=0
            elif it=="(":
                pass
            elif it in pam:
                count+=1
            else:
                pass
    inside.append(sim)
    print(max(outside),*inside)