def program6332():
    s1=["" for j in range(13)]
    s2=["" for j in range(13)]
    s=input()
    f=0
    for i in range(27):
        if f==0 and s.count(s[i])==2:
            f=1
            sp1=i
        elif f==1 and s[i]==s[sp1]:
            sp2=i
            break
    if sp2-sp1==1:
        print("Impossible")
    else:
        tp=12-(sp2-sp1-1)//2
        for i in range(27):
            if i<=sp1:
                if sp1-i<=tp:
                    s1[tp-sp1+i]=s[i]
                elif sp1-i-tp-1<=12:
                    s2[sp1-i-tp-1]=s[i]
                else:
                    s1[25-(sp1-i-tp-1)]=s[i]
            else:
                if i==sp2:
                    continue
                elif i<sp2:
                    j=i
                else:
                    j=i-1
                if tp+(j-sp1)<=12:
                    s1[tp+(j-sp1)]=s[i]
                elif 25-(tp+(j-sp1))<=12 and 25-(tp+(j-sp1))>=0:
                    s2[25-(tp+(j-sp1))]=s[i]
                else:
                    s1[abs(26-(tp+(j-sp1)))]=s[i]
        print("".join(s1))
        print("".join(s2))
                    
                