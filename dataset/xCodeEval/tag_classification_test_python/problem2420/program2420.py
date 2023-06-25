def program2420():
    #ROUNIAUDI
    i=input()
    string1=input()
    b=False
    q=""
    for u in string1:
        if u=='(' or b==True:
            q+=str(u)
            b=True
            if u==')':
                b=False
    #print(q)
    str23=q.replace('(','_').replace(')','_')
    #print(str23)
    list33=str23.split('_')
    t=list33.count('')
    ans1=len(list33)-t
    f=True
    q1=""
    for u in string1:
        if f==True and u!='(':
            q1+=str(u)
        if u=='(':
            q1+="_"
            f=False
        if u==')':
            q1+="_"
            f=True
    list34=q1.split('_')
    ans2=0
    for a in list34:
        if a!='':
           # print(a)
            ans2=max(ans2,len(a))
    print(ans2,end=" ")
    print(ans1,end=" ")