def program82():
    # -*- coding: utf-8 -*-
    """
    Created on Sat Oct 10 18:47:41 2020
    
    @author: Luke
    """
    
    s1,s2=input(),input()
     
    c=0
    for i in range(len(s1)):
        l1,l2=s1[i],s2[i]
        Ol1,Ol2=ord(l1),ord(l2)
        if Ol1==Ol2 or abs(Ol1-Ol2)==32:
            c+=1
            if c==len(s1):
                print(0)
            continue 
        if Ol1<97:
            if 65<=Ol2<Ol1 or 97<=Ol2<Ol1+32:
                print(1)
            else:
                print(-1)
            break 
        else:
            if 65<=Ol2<Ol1-32 or 97<=Ol2<Ol1:
                print(1)
            else:
                print(-1)
            break 