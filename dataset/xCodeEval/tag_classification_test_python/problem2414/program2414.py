def program2414():
    n=int(input())
    s=input()
    m1,m2=0,0
    d=[]
    p=0
    for i in s:
        if i=="_":
            if p>0:
                d.append(p)
                p=0
        elif  i=="(" or i==")":
            if p>0:
                d.append(p)
                p=0
            d.append(i)
        else:
            p+=1
    ch="AZERTYUIOPQSDFGHJKLMWXCVBN"
    if s[-1].upper()  in ch:
        d.append(p)
    if d!=[]:
        if d[0] =="(" :
            B=False
        else:
            B=True
    for i in d:
        if i=="(":
            B=False
        elif i==")":
            B=True
        elif B==False and i>0:
            m1+=1
        elif B==True and i>m2:
            m2=i
    
    print(m2,m1)